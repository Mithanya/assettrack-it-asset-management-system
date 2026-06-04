USE assettrack_db;

-- 1. Update Employees (Emails and Phones)
-- First batch of names (updated previously)
UPDATE employees SET email='ananya.s@techsolutions.in', phone='+91-9845012345' WHERE employee_name='Ananya Singh';
UPDATE employees SET email='vikram.reddy@techsolutions.in', phone='+91-9988776655' WHERE employee_name='Vikram Reddy';
UPDATE employees SET email='arjun.k@techsolutions.in', phone='+91-9876543210' WHERE employee_name='Arjun Kumar';

-- Second batch
UPDATE employees SET employee_name='Rajesh Kumar', email='rajesh.k@techsolutions.in', phone='+91-8765432109' WHERE employee_name='David Lee';
UPDATE employees SET email='priya.p@techsolutions.in', phone='+91-7654321098' WHERE employee_name='Priya Patel';
UPDATE employees SET email='rahul.d@techsolutions.in', phone='+91-6543210987' WHERE employee_name='Rahul Desai';
UPDATE employees SET email='sneha.i@techsolutions.in', phone='+91-5432109876' WHERE employee_name='Sneha Iyer';
UPDATE employees SET email='karthik.r@techsolutions.in', phone='+91-9845123456' WHERE employee_name='Karthik Raj';

-- Custom names batch
UPDATE employees SET email='mithanya@techsolutions.in', phone='+91-9845234567' WHERE employee_name='Mithanya';
UPDATE employees SET email='sridharshini@techsolutions.in', phone='+91-9845345678' WHERE employee_name='Sridharshini';
UPDATE employees SET email='kavivarshini@techsolutions.in', phone='+91-9845456789' WHERE employee_name='Kavivarshini';
UPDATE employees SET email='abi.r@techsolutions.in', phone='+91-9845567890' WHERE employee_name='Abi';
UPDATE employees SET email='kanishka.m@techsolutions.in', phone='+91-9845678901' WHERE employee_name='Kanishka';

-- Fallback for any missed fake data
UPDATE employees SET email = REPLACE(email, '@example.com', '@techsolutions.in');

-- 2. Update Assets (Realistic Serial Numbers)
UPDATE assets SET serial_number='CNU8249XYZ' WHERE serial_number='SN-DELL-1001';
UPDATE assets SET serial_number='FVF9384ZZZ' WHERE serial_number='SN-MAC-2002';
UPDATE assets SET serial_number='LTY83292AB' WHERE serial_number='SN-LOG-3003';
UPDATE assets SET serial_number='PF1J8N4B' WHERE serial_number='SN-THINK-4004';
UPDATE assets SET serial_number='MXL9204G2M' WHERE serial_number='SN-DELL-5005';
UPDATE assets SET serial_number='VNB39485XX' WHERE serial_number='SN-HP-6006';
UPDATE assets SET serial_number='DMPY6345L' WHERE serial_number='SN-IPAD-7007';
UPDATE assets SET serial_number='LZ9348JJD' WHERE serial_number='SN-ERGO-8008';

-- 3. Update Software Licenses (Realistic Keys)
UPDATE software_licenses SET license_key='W269N-WFGWX-YVC9B-4J6C9-T83GX' WHERE software_name='Windows 11 Pro';
UPDATE software_licenses SET license_key='X89B-4K9M-P2L1-Z7V3' WHERE software_name='Microsoft Office';
UPDATE software_licenses SET license_key='94F2-3B1M-L9X8-V4D1' WHERE software_name='Adobe Creative Cloud';
UPDATE software_licenses SET license_key='A1B2-C3D4-E5F6-G7H8' WHERE software_name='Adobe Photoshop';
UPDATE software_licenses SET license_key='Z93M-F82N-A1P3-T6H4' WHERE software_name='Zoom Pro';
UPDATE software_licenses SET license_key='S45D-J92K-Q8M1-C2V4' WHERE software_name='Slack Premium';
UPDATE software_licenses SET license_key='I82N-P34M-X1L9-V9D3' WHERE software_name='IntelliJ IDEA';

