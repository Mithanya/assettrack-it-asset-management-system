class ReportManager:
    """Manages various system reports using Views and Stored Procedures."""

    def __init__(self, db_manager):
        self.db = db_manager

    def department_wise_asset_report(self):
        """Fetches the department-wise asset report from the view."""
        query = "SELECT * FROM view_department_assets"
        data = self.db.fetch_all(query)
        if not data:
            print("No data available.")
            return

        print("\n--- Department-wise Asset Report ---")
        for row in data:
            print(f"Department: {row['department']} | Total Assets: {row['total_assets']} | Allocated: {row['allocated_assets']}")

    def asset_utilization_report(self):
        """Fetches the asset utilization report from the view."""
        query = "SELECT * FROM view_asset_utilization"
        data = self.db.fetch_all(query)
        if not data:
            print("No data available.")
            return

        print("\n--- Asset Utilization Report ---")
        for row in data:
            print(f"Type: {row['asset_type']} | Total: {row['total_count']} | In Use: {row['in_use']} | Available: {row['available']} | Maintenance: {row['in_maintenance']}")

    def expired_license_report(self):
        """Fetches the expired license report from the view."""
        query = "SELECT * FROM view_expired_licenses"
        data = self.db.fetch_all(query)
        if not data:
            print("No expired licenses found.")
            return

        print("\n--- Expired License Report ---")
        for row in data:
            print(f"Software: {row['software_name']} | Expiry: {row['expiry_date']} | Asset: {row['asset_name']} | Employee: {row['employee_name']}")

    def maintenance_cost_report(self, start_date, end_date):
        """Calls the stored procedure for maintenance cost report."""
        data = self.db.call_procedure('GetMaintenanceCostReport', (start_date, end_date))
        if not data:
            print(f"No maintenance records found between {start_date} and {end_date}.")
            return

        print(f"\n--- Maintenance Cost Report ({start_date} to {end_date}) ---")
        for row in data:
            print(f"Asset: {row['asset_name']} | Type: {row['asset_type']} | Total Issues: {row['total_issues']} | Total Cost: ${row['total_cost']}")
