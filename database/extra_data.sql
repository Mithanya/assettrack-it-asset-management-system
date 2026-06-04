USE assettrack_db;

-- Insert 5 Employees
INSERT INTO employees (employee_name, department, email, phone) VALUES
('David Lee', 'IT', 'david.lee@example.com', '111-222-3333'),
('Emma Watson', 'HR', 'emma.watson@example.com', '444-555-6666'),
('Frank Castle', 'Security', 'frank.castle@example.com', '777-888-9999'),
('Grace Hopper', 'Engineering', 'grace.hopper@example.com', '101-202-3030'),
('Hank Pym', 'Research', 'hank.pym@example.com', '404-505-6060');

-- Insert 5 Assets
INSERT INTO assets (asset_name, asset_type, serial_number, purchase_date, asset_status) VALUES
('ThinkPad T14', 'Laptop', 'SN-THINK-4004', '2023-08-01', 'Available'),
('Dell UltraSharp 27', 'Monitor', 'SN-DELL-5005', '2023-09-15', 'Available'),
('HP LaserJet Pro', 'Printer', 'SN-HP-6006', '2022-11-20', 'Available'),
('iPad Pro', 'Tablet', 'SN-IPAD-7007', '2024-01-10', 'Available'),
('Ergo Keyboard', 'Peripheral', 'SN-ERGO-8008', '2023-03-25', 'Available');

-- Allocate the new assets to the new employees
INSERT INTO asset_allocation (employee_id, asset_id, assigned_date) VALUES
(4, 4, '2023-08-05'),
(5, 5, '2023-09-20'),
(6, 6, '2022-12-01'),
(7, 7, '2024-01-15'),
(8, 8, '2023-04-01');

-- Update the asset status to 'Allocated'
UPDATE assets SET asset_status = 'Allocated' WHERE asset_id IN (4, 5, 6, 7, 8);

-- Insert 5 Software Licenses
INSERT INTO software_licenses (software_name, license_key, expiry_date, asset_id) VALUES
('Windows 11 Pro', 'WIN-11-ABC-1', '2026-08-01', 4),
('Adobe Photoshop', 'ADOBE-PS-2', '2025-09-15', 5),
('Zoom Pro', 'ZOOM-PRO-3', '2024-11-20', 6),
('Slack Premium', 'SLACK-PR-4', '2026-01-10', 7),
('IntelliJ IDEA', 'IDEA-PRO-5', '2025-03-25', 8);

-- Insert 5 Maintenance Records
INSERT INTO maintenance_records (asset_id, issue_description, repair_date, repair_cost) VALUES
(4, 'Screen replacement', '2023-10-01', 200.00),
(5, 'Power cable issue', '2024-01-05', 45.00),
(6, 'Paper jam sensor repair', '2023-05-15', 80.00),
(7, 'Battery replacement', '2024-02-10', 120.00),
(8, 'Key switch replaced', '2023-06-20', 25.00);
