import mysql.connector
from mysql.connector import Error
from datetime import date, datetime

# ── Database Configuration ────────────────────────────
DB_CONFIG = {
    'host'    : 'localhost',
    'user'    : 'root',
    'password': '12345',
    'database': 'assettrack_db'
}

class DatabaseManager:
    """Class to manage database connections and execute queries."""
    
    def __init__(self):
        self.host = DB_CONFIG['host']
        self.user = DB_CONFIG['user']
        self.password = DB_CONFIG['password']
        self.database = DB_CONFIG['database']
        self.connection = None

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False

    def close(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        """Execute an INSERT, UPDATE, or DELETE query."""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Failed to execute query: {e}")
            return False

    def fetch_all(self, query, params=None):
        """Execute a SELECT query and fetch all results."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Failed to fetch data: {e}")
            return []

    def call_procedure(self, proc_name, args=()):
        """Call a stored procedure."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.callproc(proc_name, args)
            results = []
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            cursor.close()
            return results
        except Error as e:
            print(f"Failed to call procedure: {e}")
            return []
