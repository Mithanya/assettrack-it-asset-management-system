USE assettrack_db;

-- Insert Employees
INSERT INTO employees (employee_name, department, email, phone) VALUES
('Alice Smith', 'IT', 'alice.smith@example.com', '123-456-7890'),
('Bob Johnson', 'HR', 'bob.johnson@example.com', '098-765-4321'),
('Charlie Brown', 'Engineering', 'charlie.brown@example.com', '555-666-7777');

-- Insert Assets
INSERT INTO assets (asset_name, asset_type, serial_number, purchase_date, asset_status) VALUES
('Dell XPS 15', 'Laptop', 'SN-DELL-1001', '2022-01-15', 'Available'),
('MacBook Pro M2', 'Laptop', 'SN-MAC-2002', '2023-05-10', 'Available'),
('Logitech Mouse', 'Peripheral', 'SN-LOG-3003', '2023-01-20', 'Available');

-- Insert Allocations
-- We assume allocating Dell XPS to Alice
INSERT INTO asset_allocation (employee_id, asset_id, assigned_date) VALUES
(1, 1, '2023-06-01');
UPDATE assets SET asset_status = 'Allocated' WHERE asset_id = 1;

-- Insert Software Licenses
INSERT INTO software_licenses (software_name, license_key, expiry_date, asset_id) VALUES
('Microsoft Office', 'OFFICE-XYZ-123', '2025-12-31', 1),
('Adobe Creative Cloud', 'ADOBE-ABC-456', '2023-12-31', 2); -- Intentionally expired for testing

-- Insert Maintenance Records
INSERT INTO maintenance_records (asset_id, issue_description, repair_date, repair_cost) VALUES
(1, 'Battery replacement', '2023-11-15', 150.00);
