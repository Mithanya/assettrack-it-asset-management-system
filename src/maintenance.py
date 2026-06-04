from datetime import date

class MaintenanceManager:
    """Manages maintenance records for assets."""

    def __init__(self, db_manager):
        self.db = db_manager

    def add_maintenance_record(self, asset_id, issue_description, repair_cost):
        """Records a maintenance issue and updates asset status."""
        repair_date = date.today()
        query1 = "INSERT INTO maintenance_records (asset_id, issue_description, repair_date, repair_cost) VALUES (%s, %s, %s, %s)"
        query2 = "UPDATE assets SET asset_status = 'In Maintenance' WHERE asset_id = %s"
        
        if self.db.execute_query(query1, (asset_id, issue_description, repair_date, repair_cost)) and self.db.execute_query(query2, (asset_id,)):
            print(f"Maintenance record added for Asset {asset_id}.")
