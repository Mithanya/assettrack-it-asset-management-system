# AssetTrack Database ER Diagram Explanation

## Overview
The **AssetTrack** database (`assettrack_db`) is designed using relational principles to manage IT assets, software licenses, maintenance records, and employee allocations. It is normalized to reduce redundancy and maintain data integrity.

## Entities and Relationships

### 1. Employees Table (`employees`)
- **Primary Key**: `employee_id`
- **Description**: Stores employee details like name, department, email, and phone.
- **Relationship**: 1-to-Many with `asset_allocation`. An employee can have multiple assets allocated to them over time.

### 2. Assets Table (`assets`)
- **Primary Key**: `asset_id`
- **Description**: Stores information about hardware assets (name, type, serial number, purchase date, and status). The status field is an ENUM allowing easy tracking ('Available', 'Allocated', 'In Maintenance', 'Retired').
- **Relationship**: 
  - 1-to-Many with `asset_allocation` (An asset can have a history of allocations).
  - 1-to-Many with `software_licenses` (An asset can have multiple software licenses installed).
  - 1-to-Many with `maintenance_records` (An asset can undergo multiple repairs).

### 3. Asset Allocation Table (`asset_allocation`)
- **Primary Key**: `allocation_id`
- **Foreign Keys**: `employee_id` (references `employees`), `asset_id` (references `assets`)
- **Description**: Acts as a junction table between `employees` and `assets`, establishing a Many-to-Many relationship over time. It tracks when an asset was assigned and when it was returned.
- **Cascading Rules**: Deletions in employee or asset tables cascade here to maintain referential integrity.

### 4. Software Licenses Table (`software_licenses`)
- **Primary Key**: `license_id`
- **Foreign Key**: `asset_id` (references `assets`)
- **Description**: Stores software names, license keys, and expiry dates. Licenses can optionally be tied to a specific hardware asset.
- **Cascading Rules**: If the related asset is deleted, `asset_id` is set to NULL rather than deleting the license, because a software license remains valid even if the hardware is retired.

### 5. Maintenance Records Table (`maintenance_records`)
- **Primary Key**: `maintenance_id`
- **Foreign Key**: `asset_id` (references `assets`)
- **Description**: Logs all repairs and maintenance activities for assets, including issue description, dates, and costs.
- **Cascading Rules**: Deleting an asset removes its maintenance history automatically.

## Summary of Advanced SQL Features Used
- **Primary & Foreign Keys**: For relational mapping.
- **ON DELETE CASCADE / SET NULL**: To gracefully handle data removal.
- **ENUM**: For defining fixed `asset_status` values.
- **Views**: Used for high-level aggregated reporting without complex repeated queries.
- **Stored Procedures**: Used for parameterized logic, like calculating maintenance cost over a specific date range.
