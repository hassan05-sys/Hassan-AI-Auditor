from flask import Flask, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

# --- CA CORE LOGIC ---
def get_audit_data():
    return {
        "revenue": 25400000,
        "expenses": 18000000,
        "tax_rate": 0.18,
        "inventory_count": 450
    }

# --- STYLES (Temporary for testing logic) ---
STYLE = """
<style>
    body { font-family: sans-serif; padding: 50px; text-align: center; background: #f4f4f4; }
    .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: inline-block; min-width: 300px; }
    .btn { display: inline-block; padding: 10px 20px; margin: 10px; text-decoration: none; color: white; border-radius: 5px; }
    .bg-green { background: #28a745; }
    .bg-blue { background: #007bff; }
    .bg-red { background: #dc3545; }
</style>
"""

@app.route('/')
def dashboard():
    return render_template_string(f"""
    <html>
        <head>{STYLE}</head>
        <body>
            <div class="card">
                <h1>HASSAN AI AUDITOR - Dashboard</h1>
                <p>Welcome, <b>HASSAN AHMED (FA25-BSAI-0089)</b></p>
                <hr>
                <a href="/inventory_audit" class="btn bg-green">Check Inventory</a>
                <a href="/tax_audit" class="btn bg-blue">Tax Report</a>
                <a href="/ledger" class="btn bg-red">Ledger Audit</a>
            </div>
        </body>
    </html>
    """)

@app.route('/inventory_audit')
def inventory_audit():
    data = get_audit_data()
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>Inventory Status</h2>
            <p>Total Items in Stock: <b>{data['inventory_count']}</b></p>
            <p>Verification Status: <span style="color:green">Verified</span></p>
            <a href="/">Back to Dashboard</a>
        </div>
    </body></html>
    """)

@app.route('/tax_audit')
def tax_audit():
    data = get_audit_data()
    profit = data['revenue'] - data['expenses']
    tax = profit * data['tax_rate']
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2>Tax Compliance Report</h2>
            <p>Gross Profit: PKR {profit}</p>
            <p>Tax Payable (18%): <b>PKR {tax}</b></p>
            <p>Status: <span style="color:blue">Filing Ready</span></p>
            <a href="/">Back to Dashboard</a>
        </div>
    </body></html>
    """)

@app.route('/ledger')
def ledger():
    return jsonify({
        "auditor": "HASSAN AHMED",
        "entries": [
            {"date": "2026-04-30", "type": "Credit", "amount": 120000, "note": "Client Payment"},
            {"date": "2026-04-30", "type": "Debit", "amount": 50000, "note": "Operational Expense"}
        ],
        "status": "Balanced"
    })

if __name__ == '__main__':
    app.run(debug=True)