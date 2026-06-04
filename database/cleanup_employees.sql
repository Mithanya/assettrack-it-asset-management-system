USE assettrack_db;

-- 1. Reset all assets to Available and clear allocations so we don't have dangling allocations
UPDATE assets SET asset_status = 'Available';
DELETE FROM asset_allocation;

-- 2. Delete all employees EXCEPT the exact 8 the user wants
-- The 8 specific ones are IDs 15 through 22
DELETE FROM employees WHERE employee_id < 15 OR employee_id > 22;

-- 3. Ensure Mithanya's department is exactly 'Software Engineering' as requested
UPDATE employees SET department = 'Software Engineering' WHERE employee_name = 'Mithanya';

-- 4. Re-allocate a few assets to the remaining employees so the project still has good report data
INSERT INTO asset_allocation (employee_id, asset_id, assigned_date) VALUES 
(15, 1, '2024-01-10'),
(16, 2, '2024-02-15'),
(17, 3, '2024-03-20');

-- 5. Update the status of those specific assets to Allocated
UPDATE assets SET asset_status = 'Allocated' WHERE asset_id IN (1, 2, 3);
