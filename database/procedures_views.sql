-- Use the database
USE assettrack_db;

-- =============================================
-- VIEWS
-- =============================================

-- View: Department-wise Asset Report
CREATE OR REPLACE VIEW view_department_assets AS
SELECT 
    e.department, 
    COUNT(a.asset_id) AS total_assets,
    SUM(CASE WHEN a.asset_status = 'Allocated' THEN 1 ELSE 0 END) AS allocated_assets
FROM 
    employees e
LEFT JOIN 
    asset_allocation aa ON e.employee_id = aa.employee_id
LEFT JOIN 
    assets a ON aa.asset_id = a.asset_id
GROUP BY 
    e.department;


-- View: Asset Utilization Report
CREATE OR REPLACE VIEW view_asset_utilization AS
SELECT 
    a.asset_type, 
    COUNT(a.asset_id) AS total_count,
    SUM(CASE WHEN a.asset_status = 'Allocated' THEN 1 ELSE 0 END) AS in_use,
    SUM(CASE WHEN a.asset_status = 'Available' THEN 1 ELSE 0 END) AS available,
    SUM(CASE WHEN a.asset_status = 'In Maintenance' THEN 1 ELSE 0 END) AS in_maintenance
FROM 
    assets a
GROUP BY 
    a.asset_type;


-- View: Expired License Report
CREATE OR REPLACE VIEW view_expired_licenses AS
SELECT 
    sl.software_name, 
    sl.license_key, 
    sl.expiry_date, 
    a.asset_name, 
    e.employee_name
FROM 
    software_licenses sl
LEFT JOIN 
    assets a ON sl.asset_id = a.asset_id
LEFT JOIN 
    asset_allocation aa ON a.asset_id = aa.asset_id
LEFT JOIN 
    employees e ON aa.employee_id = e.employee_id
WHERE 
    sl.expiry_date < CURDATE();

-- =============================================
-- STORED PROCEDURES
-- =============================================

DELIMITER //

-- Procedure: Get Maintenance Cost Report
CREATE PROCEDURE IF NOT EXISTS GetMaintenanceCostReport(IN start_date DATE, IN end_date DATE)
BEGIN
    SELECT 
        a.asset_name, 
        a.asset_type, 
        COUNT(mr.maintenance_id) AS total_issues,
        SUM(mr.repair_cost) AS total_cost
    FROM 
        assets a
    INNER JOIN 
        maintenance_records mr ON a.asset_id = mr.asset_id
    WHERE 
        mr.repair_date BETWEEN start_date AND end_date
    GROUP BY 
        a.asset_id;
END //

DELIMITER ;
