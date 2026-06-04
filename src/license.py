class LicenseManager:
    """Manages software licenses for assets."""

    def __init__(self, db_manager):
        self.db = db_manager

    def add_license(self, software_name, license_key, expiry_date, asset_id):
        """Adds a new software license and optionally links to an asset."""
        query = "INSERT INTO software_licenses (software_name, license_key, expiry_date, asset_id) VALUES (%s, %s, %s, %s)"
        success = self.db.execute_query(query, (software_name, license_key, expiry_date, asset_id))
        if success:
            print(f"License for '{software_name}' added successfully.")

    def track_expiring_licenses(self, days=30):
        """Lists licenses expiring within the next specified days."""
        query = '''
            SELECT software_name, expiry_date, asset_id 
            FROM software_licenses 
            WHERE expiry_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL %s DAY)
        '''
        licenses = self.db.fetch_all(query, (days,))
        if not licenses:
            print(f"No licenses expiring in the next {days} days.")
            return

        print(f"\n--- Licenses Expiring within {days} Days ---")
        for lic in licenses:
            print(f"Software: {lic['software_name']} | Expiry Date: {lic['expiry_date']} | Asset ID: {lic['asset_id']}")
