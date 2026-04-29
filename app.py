from flask import Flask, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

# --- CONFIGURATION ---
AUDITOR = "HASSAN AHMED"
STUDENT_ID = "FA25-BSAI-0089"

# --- THE "CA BRAIN" LOGIC ---
def get_audit_engine():
    # Real-world data simulation
    revenue = 25400000
    expenses = 18000000
    assets = 12000000
    liabilities = 4600000
    equity = 7400000
    
    profit = revenue - expenses
    
    # 1. Progressive Tax Logic (CA's main job)
    # 15% if profit < 5M, 25% if profit > 5M
    tax_rate = 0.25 if profit > 5000000 else 0.15
    tax_payable = profit * tax_rate
    
    # 2. Double-Entry Balance Check
    # Formula: Assets = Liabilities + Equity
    is_balanced = (assets == liabilities + equity)
    
    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "tax_rate": f"{tax_rate*100}%",
        "tax_payable": tax_payable,
        "is_balanced": is_balanced,
        "assets": assets,
        "liabilities": liabilities
    }

# --- STYLES ---
STYLE = """
<style>
    body { font-family: 'Segoe UI', sans-serif; background: #0a0a0a; color: white; padding: 40px; text-align: center; }
    .card { background: #161616; border: 1px solid #333; padding: 30px; border-radius: 15px; display: inline-block; text-align: left; min-width: 500px; }
    .gold { color: #d4af37; }
    .status-ok { color: #00ff41; font-weight: bold; }
    .btn { display: inline-block; padding: 10px 20px; margin: 10px 5px; background: #d4af37; color: black; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 0.8em; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    td { padding: 10px; border-bottom: 1px solid #222; }
    .header-info { margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 15px; }
</style>
"""

@app.route('/')
def dashboard():
    data = get_audit_engine()
    return render_template_string(f"""
    <html><head><title>CA AI Terminal</title>{STYLE}</head><body>
        <div class="card">
            <div class="header-info">
                <h1 class="gold" style="margin:0;">HASSAN AI AUDIT ENGINE</h1>
                <p style="color:#666;">CHIEF AUDITOR: {AUDITOR} ({STUDENT_ID})</p>
            </div>
            
            <h3>Executive Summary</h3>
            <table>
                <tr><td>Total Revenue</td><td class="status-ok">PKR {data['revenue']:,}</td></tr>
                <tr><td>Audited Expenses</td><td>PKR {data['expenses']:,}</td></tr>
                <tr><td>Net Profit</td><td class="gold">PKR {data['profit']:,}</td></tr>
                <tr><td>Tax Provision ({data['tax_rate']})</td><td style="color:#ff4d4d;">PKR {data['tax_payable']:,}</td></tr>
                <tr><td>Balance Sheet Integrity</td><td class="status-ok">{'MATCHED' if data['is_balanced'] else 'ERROR'}</td></tr>
            </table>

            <div style="margin-top:30px;">
                <a href="/inventory" class="btn">Inventory Audit</a>
                <a href="/tax_details" class="btn">Tax Compliance</a>
                <a href="/ledger" class="btn" style="background:white;">Raw Ledger (JSON)</a>
            </div>
        </div>
    </body></html>
    """)

@app.route('/inventory')
def inventory():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2 class="gold">Inventory Audit Report</h2>
            <p>Physical Stock Count: <b>450 Units</b></p>
            <p>Valuation Method: <b>FIFO (First-In, First-Out)</b></p>
            <p>Discrepancies Detected: <span class="status-ok">None</span></p>
            <br><a href="/" class="gold">Back to Dashboard</a>
        </div>
    </body></html>
    """)

@app.route('/tax_details')
def tax_details():
    data = get_audit_engine()
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="card">
            <h2 class="gold">Tax Compliance Analysis</h2>
            <p>Annual Projected Income: PKR {data['profit']:,}</p>
            <p>Applicable Tax Bracket: <b>{data['tax_rate']}</b></p>
            <p>FBR Compliance Status: <span class="status-ok">Ready for Filing</span></p>
            <hr style="border:0.5px solid #333;">
            <p style="font-size:0.8em; color:#888;">Note: This calculation is automated by {AUDITOR} AI Engine.</p>
            <br><a href="/" class="gold">Back to Dashboard</a>
        </div>
    </body></html>
    """)

@app.route('/ledger')
def ledger():
    data = get_audit_engine()
    return jsonify({
        "audit_id": "H-AI-992",
        "auditor": f"{AUDITOR} ({STUDENT_ID})",
        "balance_check": "Match" if data['is_balanced'] else "Mismatch",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "status": "Verified"
    })

if __name__ == '__main__':
    app.run(debug=True)