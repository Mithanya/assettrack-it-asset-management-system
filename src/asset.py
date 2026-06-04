from datetime import date

class AssetManager:
    """Manages IT assets and their allocations."""

    def __init__(self, db_manager):
        self.db = db_manager

    def add_asset(self, name, asset_type, serial_number, purchase_date):
        """Adds a new asset to the database."""
        query = "INSERT INTO assets (asset_name, asset_type, serial_number, purchase_date) VALUES (%s, %s, %s, %s)"
        success = self.db.execute_query(query, (name, asset_type, serial_number, purchase_date))
        if success:
            print(f"Asset '{name}' added successfully.")

    def view_assets(self):
        """Retrieves and prints all assets."""
        query = "SELECT * FROM assets"
        assets = self.db.fetch_all(query)
        if not assets:
            print("No assets found.")
            return

        print("\n--- Asset List ---")
        for asset in assets:
            print(f"ID: {asset['asset_id']} | Name: {asset['asset_name']} | Type: {asset['asset_type']} | Serial: {asset['serial_number']} | Status: {asset['asset_status']}")

    def allocate_asset(self, employee_id, asset_id):
        """Allocates an available asset to an employee."""
        # Check if asset is available
        check_query = "SELECT asset_status FROM assets WHERE asset_id = %s"
        result = self.db.fetch_all(check_query, (asset_id,))
        
        if not result:
            print("Asset not found.")
            return
            
        if result[0]['asset_status'] != 'Available':
            print("Asset is not available for allocation.")
            return
            
        # Allocate asset
        assign_date = date.today()
        query1 = "INSERT INTO asset_allocation (employee_id, asset_id, assigned_date) VALUES (%s, %s, %s)"
        query2 = "UPDATE assets SET asset_status = 'Allocated' WHERE asset_id = %s"
        
        if self.db.execute_query(query1, (employee_id, asset_id, assign_date)) and self.db.execute_query(query2, (asset_id,)):
            print(f"Asset {asset_id} successfully allocated to Employee {employee_id}.")

    def return_asset(self, asset_id):
        """Returns an allocated asset."""
        return_date = date.today()
        query1 = "UPDATE asset_allocation SET return_date = %s WHERE asset_id = %s AND return_date IS NULL"
        query2 = "UPDATE assets SET asset_status = 'Available' WHERE asset_id = %s"
        
        if self.db.execute_query(query1, (return_date, asset_id)) and self.db.execute_query(query2, (asset_id,)):
            print(f"Asset {asset_id} successfully returned.")

    def search_asset_by_employee(self, employee_id):
        """Finds all assets allocated to a specific employee."""
        query = '''
            SELECT a.asset_id, a.asset_name, a.asset_type, aa.assigned_date 
            FROM assets a 
            INNER JOIN asset_allocation aa ON a.asset_id = aa.asset_id 
            WHERE aa.employee_id = %s AND aa.return_date IS NULL
        '''
        assets = self.db.fetch_all(query, (employee_id,))
        if not assets:
            print("No active assets found for this employee.")
            return
            
        print(f"\n--- Assets for Employee {employee_id} ---")
        for asset in assets:
            print(f"Asset ID: {asset['asset_id']} | Name: {asset['asset_name']} | Type: {asset['asset_type']} | Assigned: {asset['assigned_date']}")
