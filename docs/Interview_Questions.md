# Interview Questions and Answers - AssetTrack Project

1. **What is the purpose of the AssetTrack project?**
   **Answer:** AssetTrack is a smart IT asset and license management system built to help organizations track hardware, software licenses, maintenance records, and asset allocations to employees effectively using a Python CLI and MySQL backend.

2. **Why did you choose Python and MySQL for this project?**
   **Answer:** Python was chosen for its simplicity, readability, and robust database connectors (`mysql-connector-python`), making it ideal for CLI apps and business logic. MySQL was chosen because it is a reliable, open-source relational database that excellently handles structured data and complex joins.

3. **Can you explain the Object-Oriented Programming (OOP) concepts used in your project?**
   **Answer:** The project uses Encapsulation and Abstraction by grouping related functions into specific manager classes (e.g., `EmployeeManager`, `AssetManager`). The database connection logic is abstracted into a `DatabaseManager` class, decoupling database operations from business logic.

4. **How do you handle exceptions in your Python code?**
   **Answer:** I used `try-except` blocks. For example, in the `DatabaseManager` class, queries are wrapped in `try` blocks, catching `mysql.connector.Error` exceptions to prevent application crashes when a database issue occurs and instead printing a user-friendly error message. In the `main.py` entry point, a generic try-except catches all unexpected errors.

5. **What is the role of `mysql-connector-python`?**
   **Answer:** It is the official Oracle-supported driver for connecting Python applications to MySQL databases. It allows the Python code to send SQL queries to the MySQL server and retrieve results in Python data structures (like tuples or dictionaries).

6. **What is normalization, and how is it applied in your database schema?**
   **Answer:** Normalization is the process of organizing data to reduce redundancy and improve data integrity. In AssetTrack, data is divided into logical tables (employees, assets, licenses). The `asset_allocation` table acts as a bridge to manage the many-to-many relationship between employees and assets over time (3NF).

7. **Explain the difference between INNER JOIN and LEFT JOIN. Which one did you use and why?**
   **Answer:** `INNER JOIN` returns only records that have matching values in both tables, while `LEFT JOIN` returns all records from the left table and the matched records from the right table (or NULL if no match). I used `INNER JOIN` to fetch maintenance records for existing assets, and `LEFT JOIN` in the Department-wise Report View to include all employees even if they don't have an asset allocated.

8. **What is a Primary Key and a Foreign Key? Give an example from your project.**
   **Answer:** A Primary Key uniquely identifies a record in a table (e.g., `employee_id` in the `employees` table). A Foreign Key is a field in one table that links to the primary key of another table. For example, `employee_id` in the `asset_allocation` table is a foreign key linking to the `employees` table.

9. **What are SQL Views, and why did you use them in AssetTrack?**
   **Answer:** A View is a virtual table based on the result-set of an SQL statement. I used views for complex reports like `view_asset_utilization` and `view_expired_licenses` to simplify the Python code. Instead of writing complex `GROUP BY` and `JOIN` queries in Python, the logic is stored in the database, and Python simply runs `SELECT * FROM view_name`.

10. **What is a Stored Procedure, and how is it different from a View?**
    **Answer:** A View is essentially a saved query that acts like a table, while a Stored Procedure is a saved batch of SQL statements that can accept parameters and execute complex procedural logic. I used a Stored Procedure (`GetMaintenanceCostReport`) because it needed input parameters (`start_date` and `end_date`), which views cannot accept.

11. **How did you implement the "Allocate Asset" feature?**
    **Answer:** The `allocate_asset` function first checks if the asset exists and its status is 'Available'. If so, it performs two database operations: it inserts a record into the `asset_allocation` table with the current date, and it updates the `assets` table to change the status to 'Allocated'. 

12. **What is the significance of the `ON DELETE CASCADE` rule in your foreign keys?**
    **Answer:** `ON DELETE CASCADE` ensures referential integrity. If an `employee` is deleted, all their related records in the `asset_allocation` table are automatically deleted by the database, preventing orphaned records.

13. **Why did you use `ON DELETE SET NULL` for software licenses instead of CASCADE?**
    **Answer:** If an asset is retired and deleted, the software license purchased for it might still be valid and could be re-assigned to a different machine. Setting the `asset_id` to `NULL` keeps the license in the system while unlinking it from the deleted hardware.

14. **How do you track software licenses that are about to expire?**
    **Answer:** I created a Python function that uses a SQL query with the `BETWEEN` and `DATE_ADD` functions. The query checks if the `expiry_date` falls between `CURDATE()` and a user-defined number of days in the future (e.g., 30 days).

15. **What would happen if the database connection fails in your application?**
    **Answer:** The `DatabaseManager.connect()` method is called at the start of the program. If it fails (caught by try-except), it returns `False`, and the `main.py` script gracefully exits with a message rather than allowing the application to run and crash on the first database operation.

16. **What is the purpose of `cursor.execute()` and `cursor.fetchall()`?**
    **Answer:** `cursor.execute()` is used to send a specific SQL command to the MySQL server. `cursor.fetchall()` is used after a `SELECT` query to retrieve all the rows returned by the query into a Python list.

17. **How do you prevent SQL Injection in your Python application?**
    **Answer:** By using parameterized queries. Instead of formatting strings with variables (e.g., `f"SELECT * FROM table WHERE id={user_input}"`), I use `%s` placeholders and pass the variables as a tuple to `execute()`. The MySQL connector safely escapes the inputs, preventing SQL injection.

18. **Explain the `GROUP BY` clause and an Aggregate function used in your project.**
    **Answer:** `GROUP BY` is used to group rows that have the same values into summary rows. Aggregate functions perform a calculation on a set of values. In my project, I used `GROUP BY e.department` with the `COUNT()` aggregate function to find the total number of assets per department.

19. **How would you scale this application in the future?**
    **Answer:** For future scaling, I would replace the CLI with a web interface using a framework like Flask or Django. I would implement an ORM (like SQLAlchemy) for better database abstraction. I would also add user authentication/authorization (Admin vs Employee roles).

20. **What was the most challenging part of this project, and how did you overcome it?**
    **Answer:** The most challenging part was ensuring data consistency when allocating and returning assets (e.g., making sure an allocated asset cannot be allocated again). I overcame this by implementing strict checks in the Python logic before executing updates and using transactions (committing only after both the status update and the allocation insert succeed).
