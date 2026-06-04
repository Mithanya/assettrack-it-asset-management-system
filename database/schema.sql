-- Create database
CREATE DATABASE IF NOT EXISTS assettrack_db;
USE assettrack_db;

-- 1. employees
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

-- 2. assets
CREATE TABLE IF NOT EXISTS assets (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    asset_type VARCHAR(50) NOT NULL,
    serial_number VARCHAR(100) UNIQUE NOT NULL,
    purchase_date DATE,
    asset_status ENUM('Available', 'Allocated', 'In Maintenance', 'Retired') DEFAULT 'Available'
);

-- 3. asset_allocation
CREATE TABLE IF NOT EXISTS asset_allocation (
    allocation_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    asset_id INT,
    assigned_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE CASCADE
);

-- 4. software_licenses
CREATE TABLE IF NOT EXISTS software_licenses (
    license_id INT AUTO_INCREMENT PRIMARY KEY,
    software_name VARCHAR(100) NOT NULL,
    license_key VARCHAR(255) UNIQUE NOT NULL,
    expiry_date DATE NOT NULL,
    asset_id INT,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE SET NULL
);

-- 5. maintenance_records
CREATE TABLE IF NOT EXISTS maintenance_records (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    issue_description TEXT NOT NULL,
    repair_date DATE NOT NULL,
    repair_cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE CASCADE
);
