# AssetTrack IT Asset Management System

## Overview
AssetTrack is a command‑line application for managing IT assets, software licenses, and employee allocations. It provides a menu‑driven interface to add, view, allocate, and report on assets, licenses, and maintenance records.

## Features
- Add, view, and delete employee records
- Manage hardware assets (laptops, monitors, peripherals, etc.)
- Allocate and return assets to employees
- Track software licenses with realistic keys
- Record maintenance activities and generate cost reports
- Generate departmental and utilization reports
- Search assets by employee and monitor expiring licenses

## Prerequisites
- Python 3.10 or higher
- MySQL server (or compatible MariaDB) with a database named `assettrack_db`
- `mysql` command‑line client available in the system PATH

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Mithanya/assettrack-it-asset-management-system.git
   cd assettrack-it-asset-management-system
   ```
2. Set up the virtual environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```
3. Create the database and import the initial schema:
   ```
   mysql -u root -p12345 < database\schema.sql
   ```
4. Populate the database with realistic mock data:
   ```
   mysql -u root -p12345 < database\anonymize_data.sql
   ```

## Usage
Run the wrapper script from the project root:
```powershell
python main.py
```
The menu will be displayed. For example, selecting **4** shows the list of all assets, and **2** displays employee details.

## Database Structure
- `employees` – employee ID, name, email, and department
- `assets` – asset ID, name, type, serial number, and status
- `software_licenses` – license key, software name, and expiration
- `maintenance_records` – asset ID, description, cost, and date

## Contributing
1. Fork the repository and create a new branch for your feature or bug fix.
2. Ensure the code follows PEP 8 guidelines and that existing tests pass.
3. Submit a pull request with a clear description of changes.

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, open an issue on the GitHub repository or contact the author at `mithanya@techsolutions.in`.
