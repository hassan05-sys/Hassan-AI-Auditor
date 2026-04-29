import sqlite3

def init_db():
    conn = sqlite3.connect('Audit_Master.db')
    cursor = conn.cursor()
    
    # 1. Master Ledger (Operational Tasks)
    cursor.execute('''CREATE TABLE IF NOT EXISTS ledger (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        account_name TEXT,
        category TEXT,
        debit REAL DEFAULT 0,
        credit REAL DEFAULT 0,
        description TEXT
    )''')

    # 2. Tax & Compliance Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS tax_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        month TEXT,
        total_sales REAL,
        output_tax REAL,
        input_tax REAL,
        payable_gst REAL
    )''')

    # 3. Payroll Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS payroll (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id TEXT,
        name TEXT,
        basic_salary REAL,
        allowances REAL,
        tax_deduction REAL,
        net_salary REAL
    )''')

    conn.commit()
    conn.close()
    print("✅ Audit Database Engine Initialized.")

if __name__ == "__main__":
    init_db()