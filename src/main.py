import sys
from db import DatabaseManager
from employee import EmployeeManager
from asset import AssetManager
from license import LicenseManager
from maintenance import MaintenanceManager
from reports import ReportManager

def main_menu():
    print("\n" + "="*50)
    print("AssetTrack - Smart IT Asset & License Management")
    print("="*50)
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Add Asset")
    print("4. View Assets")
    print("5. Allocate Asset to Employee")
    print("6. Return Asset")
    print("7. Add Software License")
    print("8. Track Expiring Licenses")
    print("9. Add Maintenance Record")
    print("10. Search Asset by Employee")
    print("11. Department-wise Asset Report")
    print("12. Asset Utilization Report")
    print("13. Expired License Report")
    print("14. Maintenance Cost Report")
    print("15. Exit")
    print("="*50)
    
    choice = input("Enter your choice (1-15): ")
    return choice

def main():
    db = DatabaseManager()
    if not db.connect():
        print("Failed to start application. Database connection error.")
        sys.exit(1)

    emp_mgr = EmployeeManager(db)
    asset_mgr = AssetManager(db)
    lic_mgr = LicenseManager(db)
    maint_mgr = MaintenanceManager(db)
    rep_mgr = ReportManager(db)

    try:
        while True:
            choice = main_menu()
            
            if choice == '1':
                name = input("Enter Employee Name: ")
                dept = input("Enter Department: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                emp_mgr.add_employee(name, dept, email, phone)
                
            elif choice == '2':
                emp_mgr.view_employees()
                
            elif choice == '3':
                name = input("Enter Asset Name: ")
                atype = input("Enter Asset Type (e.g. Laptop, Peripheral): ")
                serial = input("Enter Serial Number: ")
                pdate = input("Enter Purchase Date (YYYY-MM-DD): ")
                asset_mgr.add_asset(name, atype, serial, pdate)
                
            elif choice == '4':
                asset_mgr.view_assets()
                
            elif choice == '5':
                emp_id = int(input("Enter Employee ID: "))
                asset_id = int(input("Enter Asset ID: "))
                asset_mgr.allocate_asset(emp_id, asset_id)
                
            elif choice == '6':
                asset_id = int(input("Enter Asset ID to Return: "))
                asset_mgr.return_asset(asset_id)
                
            elif choice == '7':
                name = input("Enter Software Name: ")
                key = input("Enter License Key: ")
                expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
                asset_id = input("Enter Asset ID (or leave blank if None): ")
                asset_id = int(asset_id) if asset_id else None
                lic_mgr.add_license(name, key, expiry, asset_id)
                
            elif choice == '8':
                days = int(input("Enter number of days to check for expiry: "))
                lic_mgr.track_expiring_licenses(days)
                
            elif choice == '9':
                asset_id = int(input("Enter Asset ID: "))
                issue = input("Enter Issue Description: ")
                cost = float(input("Enter Repair Cost: "))
                maint_mgr.add_maintenance_record(asset_id, issue, cost)
                
            elif choice == '10':
                emp_id = int(input("Enter Employee ID: "))
                asset_mgr.search_asset_by_employee(emp_id)
                
            elif choice == '11':
                rep_mgr.department_wise_asset_report()
                
            elif choice == '12':
                rep_mgr.asset_utilization_report()
                
            elif choice == '13':
                rep_mgr.expired_license_report()
                
            elif choice == '14':
                sdate = input("Enter Start Date (YYYY-MM-DD): ")
                edate = input("Enter End Date (YYYY-MM-DD): ")
                rep_mgr.maintenance_cost_report(sdate, edate)
                
            elif choice == '15':
                print("Exiting AssetTrack System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
