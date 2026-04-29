from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <body style="font-family: Arial; text-align: center; background-color: #f4f4f4; padding: 50px;">
            <h1 style="color: #2c3e50;">HASSAN AI AUDITOR - Dashboard</h1>
            <p>Welcome, <b>HASSAN AHMED (FA25-BSAI-0089)</b></p>
            <hr style="width: 50%;">
            <div style="margin-top: 20px;">
                <a href="/inventory_audit" style="padding: 10px 20px; background: #27ae60; color: white; text-decoration: none; border-radius: 5px; margin: 5px;">Check Inventory</a>
                <a href="/tax_audit" style="padding: 10px 20px; background: #2980b9; color: white; text-decoration: none; border-radius: 5px; margin: 5px;">Tax Report</a>
                <a href="/fraud_check" style="padding: 10px 20px; background: #e74c3c; color: white; text-decoration: none; border-radius: 5px; margin: 5px;">Fraud Scanner</a>
            </div>
        </body>
    </html>
    """

@app.route('/inventory_audit')
def inventory_audit():
    stock = [
        {"item": "Handmade Rings", "quantity": 120, "unit_price": 500},
        {"item": "Designer Watches", "quantity": 15, "unit_price": 12000}
    ]
    total_value = sum(item['quantity'] * item['unit_price'] for item in stock)
    return jsonify({"developer": "HASSAN AHMED", "total_valuation": total_value, "data": stock})

@app.route('/tax_audit')
def tax_audit():
    revenue = 2500000
    tax = revenue * 0.18
    return jsonify({"developer": "HASSAN AHMED", "gross_revenue": revenue, "gst_payable_18pc": tax})

@app.route('/fraud_check')
def fraud_check():
    return jsonify({"status": "Safe", "alerts": 0, "auditor": "HASSAN AHMED"})

if __name__ == '__main__':
    app.run(debug=True)