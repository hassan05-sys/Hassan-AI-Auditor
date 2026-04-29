from flask import Flask, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('Audit_Master.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            student_id TEXT,
            activity TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Initial log entry for HASSAN AHMED
    cursor.execute("INSERT INTO audit_logs (user_name, student_id, activity) VALUES (?, ?, ?)", 
                   ('HASSAN AHMED', 'FA25-BSAI-0089', 'Server Started - Full Audit Suite'))
    conn.commit()
    conn.close()

# Initialize DB on start
init_db()

@app.route('/')
def home():
    return jsonify({
        "status": "Online",
        "developer": "HASSAN AHMED",
        "id": "FA25-BSAI-0089",
        "university": "MAJU",
        "message": "Welcome to HASSAN AI - The Future of Global Auditing",
        "endpoints": {
            "inventory": "/inventory_audit",
            "tax": "/tax_audit",
            "fraud_scanner": "/fraud_check"
        }
    })

@app.route('/inventory_audit')
def inventory_audit():
    # CA Module: Stock Valuation
    stock = [
        {"item": "Handmade Rings", "quantity": 120, "unit_price": 500},
        {"item": "Designer Watches", "quantity": 15, "unit_price": 12000},
        {"item": "Luxury Bracelets", "quantity": 45, "unit_price": 2500}
    ]
    total_value = sum(item['quantity'] * item['unit_price'] for item in stock)
    return jsonify({
        "module": "Inventory Auditor",
        "total_valuation_pkr": total_value,
        "items_scanned": len(stock),
        "data": stock
    })

@app.route('/tax_audit')
def tax_audit():
    # Tax Module: FBR Simulation (18% GST)
    revenue = 2500000 # 25 Lakh
    gst_rate = 0.18
    tax_amount = revenue * gst_rate
    return jsonify({
        "module": "Tax Calculator",
        "entity": "HASSAN AHMED (FA25-BSAI-0089)",
        "gross_revenue": revenue,
        "gst_payable_18pc": tax_amount,
        "net_revenue": revenue - tax_amount
    })

@app.route('/fraud_check')
def fraud_check():
    # Security Module: Anomaly Detection
    alerts = [
        {"type": "Duplicate Payment", "amount": 45000, "status": "Flagged"},
        {"type": "Suspicious Night Transfer", "amount": 120000, "status": "Pending Verification"}
    ]
    return jsonify({
        "module": "AI Fraud Scanner",
        "alerts_found": len(alerts),
        "risk_score": "78/100",
        "findings": alerts
    })

if __name__ == '__main__':
    app.run(debug=True)