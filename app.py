from flask import Flask, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

# --- CORE SETTINGS ---
FIRM_NAME = "HASSAN AI AUDITORS"
AUDITOR_IDENTITY = "HASSAN AHMED (FA25-BSAI-0089)"

def get_live_data():
    return {
        "revenue": 25400000,
        "expenses": 18000000,
        "tax_rate": 0.18,
        "assets": 12000000,
        "liabilities": 4600000
    }

# --- PREMIUM CORPORATE STYLES ---
STYLE = """
<style>
    :root { --gold: #d4af37; --bg: #0a0a0a; --card: #161616; --text: #f0f0f0; }
    body { background-color: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; margin: 0; padding: 40px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
    .glass-card { background: var(--card); border: 1px solid #333; padding: 40px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); width: 100%; max-width: 800px; text-align: center; }
    h1 { color: var(--gold); letter-spacing: 4px; font-weight: 300; text-transform: uppercase; margin-bottom: 5px; }
    .identity { color: #666; font-size: 0.8em; letter-spacing: 2px; margin-bottom: 40px; border-bottom: 1px solid #222; padding-bottom: 20px; }
    
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 40px; }
    .stat-box { background: #1f1f1f; padding: 20px; border-radius: 12px; border: 1px solid #2a2a2a; transition: 0.3s; cursor: default; }
    .stat-box:hover { border-color: var(--gold); transform: translateY(-5px); }
    .label { font-size: 0.7em; color: #888; text-transform: uppercase; margin-bottom: 5px; }
    .value { font-size: 1.4em; color: white; font-weight: bold; }

    .btn-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; }
    .btn { text-decoration: none; padding: 12px 25px; border-radius: 8px; font-size: 0.8em; font-weight: bold; letter-spacing: 1px; transition: 0.3s; text-transform: uppercase; border: 1px solid transparent; }
    .btn-gold { background: var(--gold); color: black; }
    .btn-outline { border-color: #333; color: white; }
    .btn:hover { opacity: 0.8; transform: scale(1.05); }

    .footer { margin-top: 50px; font-size: 0.7em; color: #444; text-transform: uppercase; }
</style>
"""

@app.route('/')
def home():
    data = get_live_data()
    profit = data['revenue'] - data['expenses']
    return render_template_string(f"""
    <html>
        <head><title>Executive Audit Terminal</title>{STYLE}</head>
        <body>
            <div class="glass-card">
                <h1>{FIRM_NAME}</h1>
                <div class="identity">CHIEF AUDITOR: {AUDITOR_IDENTITY}</div>
                
                <div class="grid">
                    <div class="stat-box"><div class="label">Total Volume</div><div class="value">PKR {data['revenue']:,}</div></div>
                    <div class="stat-box"><div class="label">Audited Profit</div><div class="value" style="color:#00ff41;">PKR {profit:,}</div></div>
                    <div class="stat-box"><div class="label">Compliance</div><div class="value">100% SECURE</div></div>
                </div>

                <div class="btn-container">
                    <a href="/audit_report" class="btn btn-gold">Generate Report</a>
                    <a href="/fraud_scanner" class="btn btn-outline">Risk Analysis</a>
                    <a href="/ledger" class="btn btn-outline" style="border-color:#ff4d4d; color:#ff4d4d;">Audit Ledger</a>
                </div>

                <div class="footer">Encrypted Session // Protocol V4.2 // Karachi Office</div>
            </div>
        </body>
    </html>
    """)

@app.route('/audit_report')
def report():
    data = get_live_data()
    profit = data['revenue'] - data['expenses']
    tax = profit * data['tax_rate']
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="glass-card" style="text-align:left;">
            <h2 style="color:var(--gold);">CERTIFIED AUDIT REPORT</h2>
            <hr style="border:0; border-top:1px solid #222; margin:20px 0;">
            <p>Net Liquidity: <b>PKR {profit:,}</b></p>
            <p>Taxation Provision: <b>PKR {tax:,.0f}</b></p>
            <p>Status: <span style="color:#00ff41;">Verified by HASSAN AI</span></p>
            <br>
            <a href="/" class="btn btn-outline">Back to Terminal</a>
        </div>
    </body></html>
    """)

@app.route('/fraud_scanner')
def scanner():
    return render_template_string(f"""
    <html><head>{STYLE}</head><body>
        <div class="glass-card">
            <h2 style="color:#ff4d4d;">AI ANOMALY DETECTION</h2>
            <p style="color:#888;">Scanning all nodes for financial discrepancies...</p>
            <div style="background:#111; padding:20px; border-radius:10px; border-left:4px solid #ff4d4d; text-align:left;">
                <span style="color:#ff4d4d;">[WARNING]</span> Unusual high-value transaction detected in Ledger Entry #AX-902.
            </div>
            <br>
            <a href="/" class="btn btn-outline">Return to Safety</a>
        </div>
    </body></html>
    """)

@app.route('/ledger')
def ledger_json():
    data = get_live_data()
    return jsonify({
        "audit_id": "H-AI-992",
        "auditor": f"{AUDITOR_IDENTITY}",
        "balance_check": "Match",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "verdict": "Clear for Filing"
    })

if __name__ == '__main__':
    app.run(debug=True)