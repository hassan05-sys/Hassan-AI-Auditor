from flask import Flask, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

# --- ADVANCED CA LOGIC MODULE ---
class ProfessionalAuditor:
    def __init__(self, revenue, expenses):
        self.revenue = revenue
        self.expenses = expenses
        self.audit_id = "AUD-2026-001"

    def get_tax_bracket(self, profit):
        # Professional Tax Logic: 15% for < 5M, 25% for > 5M
        return 0.15 if profit < 5000000 else 0.25

    def generate_ca_summary(self):
        gross_profit = self.revenue - self.expenses
        rate = self.get_tax_bracket(gross_profit)
        tax_amount = gross_profit * rate
        
        return {
            "auditor_signature": "HASSAN AHMED (FA25-BSAI-0089)",
            "verification_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "core_financials": {
                "total_revenue": self.revenue,
                "total_deductions": self.expenses,
                "taxable_income": gross_profit,
                "applied_tax_rate": f"{rate*100}%",
                "net_payable_tax": tax_amount
            },
            "ca_health_check": {
                "profit_margin": f"{(gross_profit/self.revenue)*100:.2f}%",
                "liquidity_status": "Highly Liquid" if gross_profit > 1000000 else "Critical",
                "audit_verdict": "UNQUALIFIED OPINION (Clean Record)"
            }
        }

# Initialize with sample data
ca_system = ProfessionalAuditor(revenue=25400000, expenses=18000000)

# --- ROUTES ---

@app.route('/')
def home():
    # Simple UI to link all CA endpoints
    return render_template_string("""
        <body style="font-family: Arial; text-align: center; padding-top: 50px; background: #f9f9f9;">
            <h1>HASSAN AI - CA CORE ENGINE</h1>
            <p>Status: <span style="color: green;"><b>OPERATIONAL</b></span></p>
            <div style="margin-top: 30px;">
                <a href="/api/v1/full_audit" style="padding: 10px; background: #333; color: white; text-decoration: none; border-radius: 5px;">View Detailed Audit</a>
                <a href="/api/v1/ledger" style="padding: 10px; background: #d4af37; color: black; text-decoration: none; border-radius: 5px;">View General Ledger</a>
            </div>
            <p style="margin-top: 50px; color: #888;">Developer: HASSAN AHMED (FA25-BSAI-0089)</p>
        </body>
    """)

@app.route('/api/v1/full_audit')
def full_audit():
    return jsonify(ca_system.generate_ca_summary())

@app.route('/api/v1/ledger')
def ledger():
    # Double-entry simulation
    ledger_data = [
        {"ref": "TR-001", "account": "Cash", "debit": 500000, "credit": 0},
        {"ref": "TR-002", "account": "Accounts Payable", "debit": 0, "credit": 200000},
        {"ref": "TR-003", "account": "Equity", "debit": 0, "credit": 300000}
    ]
    return jsonify({
        "ledger_name": "General Ledger 2026",
        "auditor": "HASSAN AHMED",
        "entries": ledger_data,
        "is_balanced": sum(x['debit'] for x in ledger_data) == sum(x['credit'] for x in ledger_data)
    })

if __name__ == '__main__':
    app.run(debug=True)