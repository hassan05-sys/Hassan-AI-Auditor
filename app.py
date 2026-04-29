from flask import Flask, render_template_string, jsonify, request
from datetime import datetime

app = Flask(__name__)

# --- CA SETTINGS & DATA ---
FIRM_NAME = "HASSAN AI AUDITORS"
AUDITOR_ID = "FA25-BSAI-0089"

def get_financial_context():
    return {
        "revenue": 25400000,
        "expenses": 18000000,
        "assets": 12000000,
        "liabilities": 4600000,
        "inventory": 450
    }

# --- STYLES ---
STYLE = """
<style>
    body { font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: #e0e0e0; text-align: center; padding: 40px; }
    .container { max-width: 900px; margin: auto; background: #1a1a1a; padding: 30px; border-radius: 15px; border: 1px solid #333; }
    .gold { color: #d4af37; }
    .btn { display: inline-block; padding: 12px 25px; margin: 10px; text-decoration: none; color: #000; background: #d4af37; border-radius: 5px; font-weight: bold; transition: 0.3s; }
    .btn:hover { background: #fff; transform: translateY(-2px); }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; text-align: left; }
    th, td { padding: 12px; border-bottom: 1px solid #333; }
    .risk-high { color: #ff4d4d; font-weight: bold; }
    .risk-low { color: #00ff41; }
</style>
"""

@app.route('/')
def dashboard():
    return render_template_string(f"""
    <html>
        <head><title>CA Terminal</title>{STYLE}</head>
        <body>
            <div class="container">
                <h1 class="gold">{FIRM_NAME}</h1>
                <p>Lead Auditor: <b>HASSAN AHMED ({AUDITOR_ID})</b></p>
                <hr style="border: 0.5px solid #333;">
                <div style="margin: 30px 0;">
                    <a href="/audit_report" class="btn">Generate Audit Report</a>
                    <a href="/fraud_scanner" class="btn" style="background:#ff4d4d;">Run Fraud Scan</a>
                    <a href="/ledger" class="btn" style="background:#fff;">View General Ledger</a>
                </div>
                <p style="font-size: 0.8em; color: #666;">System Status: Secure & Synchronized</p>
            </div>
        </body>
    </html>
    """)

@app.route('/audit_report')
def audit_report():
    data = get_financial_context()
    profit = data['revenue'] - data['expenses']
    # CA Logic: Progressive Tax
    tax_rate = 0.25 if profit > 5000000 else 0.15
    tax_amount = profit * tax_rate
    
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="container">
            <h2 class="gold">Executive Audit Summary</h2>
            <table>
                <tr><td>Gross Revenue</td><td>PKR {data['revenue']:,}</td></tr>
                <tr><td>Total Expenses</td><td>PKR {data['expenses']:,}</td></tr>
                <tr><td>Net Profit</td><td class="risk-low">PKR {profit:,}</td></tr>
                <tr><td>Tax Liability ({int(tax_rate*100)}%)</td><td style="color:#ff9f43;">PKR {tax_amount:,}</td></tr>
            </table>
            <p style="margin-top:20px;">Verdict: <span class="risk-low">Unqualified Opinion (Clean)</span></p>
            <a href="/" style="color:#d4af37;">Return to Terminal</a>
        </div>
    </body></html>
    """)

@app.route('/fraud_scanner')
def fraud_scanner():
    # Simulation of CA Anomaly Detection
    anomalies = [
        {"ref": "EXP-402", "item": "Office Supplies", "amount": 850000, "risk": "High", "reason": "Deviation from mean > 400%"},
        {"ref": "EXP-405", "item": "Travel Expense", "amount": 12000, "risk": "Low", "reason": "Standard entry"}
    ]
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="container">
            <h2 style="color:#ff4d4d;">AI Fraud Detection Scan</h2>
            <table>
                <tr><th>Ref ID</th><th>Category</th><th>Amount</th><th>Risk Level</th></tr>
                {"".join([f"<tr><td>{a['ref']}</td><td>{a['item']}</td><td>{a['amount']}</td><td class='risk-{'high' if a['risk']=='High' else 'low'}'>{a['risk']}</td></tr>" for a in anomalies])}
            </table>
            <br><a href="/" style="color:#d4af37;">Back to Safety</a>
        </div>
    </body></html>
    """)

@app.route('/ledger')
def ledger():
    data = get_financial_context()
    return jsonify({
        "audit_id": "H-AI-992",
        "auditor": "HASSAN AHMED",
        "balance_check": "Match" if data['assets'] == (data['liabilities'] + (data['revenue']-data['expenses'])) else "Review Needed",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

if __name__ == '__main__':
    app.run(debug=True)