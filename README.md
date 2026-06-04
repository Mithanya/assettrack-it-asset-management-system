# AssetTrack – IT Asset Management System

## Overview

AssetTrack is a Python and MySQL-based IT Asset Management System designed to streamline the tracking and management of organizational IT assets. The system enables efficient asset allocation, software license monitoring, maintenance tracking, and report generation through a user-friendly menu-driven interface.

This project simulates a real‑world enterprise asset management solution used by organizations to manage hardware resources and software licenses effectively.

---

## Key Features

### Employee Management

* Add and manage employee records
* Store employee details including department and contact information
* View employee information

### Asset Management

* Register and track IT assets
* Manage asset details such as type, serial number, purchase date, and status
* View available and allocated assets

### Asset Allocation

* Assign assets to employees
* Return allocated assets
* Maintain allocation history

### Software License Management

* Store software license information
* Monitor license expiry dates
* Generate expired and expiring license reports

### Maintenance Tracking

* Record maintenance activities
* Track repair costs and service history
* Generate maintenance reports

### Reporting & Analytics

* Department‑wise Asset Report
* Asset Utilization Report
* Maintenance Cost Report
* Expired License Report
* Employee Asset Search

---

## Technologies Used

* Python 3
* MySQL
* MySQL Connector for Python
* SQL
* Git
* GitHub

---

## Database Modules

### Employees

Stores employee information.

### Assets

Stores hardware asset details.

### Asset Allocation

Maintains asset assignment records.

### Software Licenses

Tracks software licenses and expiry dates.

### Maintenance Records

Stores maintenance and repair history.

---

## Project Structure

```text
assettrack-it-asset-management-system/
│
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── docs/
│
├── src/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Mithanya/assettrack-it-asset-management-system.git
cd assettrack-it-asset-management-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Database

```sql
CREATE DATABASE assettrack_db;
```

### Import Database Schema

```bash
mysql -u root -p < database/schema.sql
```

### Run Application

```bash
python main.py
```

---

## Sample Functionalities

* Add Employee
* View Employees
* Add Asset
* View Assets
* Allocate Asset to Employee
* Return Asset
* Add Software License
* Track Expiring Licenses
* Add Maintenance Record
* Search Asset by Employee
* Department‑wise Asset Report
* Asset Utilization Report
* Expired License Report
* Maintenance Cost Report

---

## Concepts Implemented

* Relational Database Design
* Primary Keys and Foreign Keys
* SQL Joins
* CRUD Operations
* Aggregate Functions
* Database Connectivity
* Exception Handling
* Menu‑Driven Programming
* Reporting and Analytics

---

## Future Enhancements

* Graphical User Interface (Tkinter)
* Web‑Based Dashboard using Flask
* User Authentication System
* Email Alerts for License Expiry
* Asset Analytics Dashboard
* Role‑Based Access Control

---

## Project Objective

The objective of AssetTrack is to provide an efficient solution for managing organizational IT assets, software licenses, and maintenance activities while improving visibility, accountability, and resource utilization.

---

## Author

**Mithanya Murugesan**

GitHub: https://github.com/Mithanya

LinkedIn: https://www.linkedin.com/in/mithanya-murugesan/
