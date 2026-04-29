from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# --- CA CORE LOGIC (The Brain) ---

class CAAICore:
    def __init__(self):
        self.revenue = 25400000
        self.expenses = 18000000
        self.tax_rate = 0.18 # 18% GST/Sales Tax
        
    def calculate_audit(self):
        gross_profit = self.revenue - self.expenses
        tax_payable = gross_profit * self.tax_rate
        net_income = gross_profit - tax_payable
        
        # CA Insight: Identifying efficiency
        efficiency_ratio = (self.expenses / self.revenue) * 100
        
        return {
            "financial_summary": {
                "gross_revenue": self.revenue,
                "total_expenses": self.expenses,
                "tax_liability": tax_payable,
                "net_profit": net_income
            },
            "ca_metrics": {
                "profit_margin": f"{((gross_profit/self.revenue)*100):.2f}%",
                "efficiency_ratio": f"{efficiency_ratio:.2f}%",
                "status": "Balanced" if self.revenue > self.expenses else "Deficit"
            }
        }

ca_engine = CAAICore()

# --- ROUTES (The Functions) ---

@app.route('/')
def health_check():
    return {
        "system": "HASSAN AI CA-ENGINE",
        "developer": "HASSAN AHMED (FA25-BSAI-0089)",
        "status": "Operational",
        "endpoints": ["/api/v1/full_audit", "/api/v1/tax_report", "/api/v1/ledger"]
    }

@app.route('/api/v1/full_audit')
def full_audit():
    # Simulated full business audit
    report = ca_engine.calculate_audit()
    return jsonify({
        "timestamp": datetime.now().isoformat(),
        "auditor": "HASSAN AHMED",
        "data": report
    })

@app.route('/api/v1/tax_report')
def tax_report():
    # Focused on Tax Compliance
    data = ca_engine.calculate_audit()
    tax_info = {
        "tax_payable": data['financial_summary']['tax_liability'],
        "tax_period": "Q1 2026",
        "compliance_status": "Verified",
        "ca_recommendation": "Maintain 18% reserve for FBR compliance."
    }
    return jsonify(tax_info)

@app.route('/api/v1/ledger')
def ledger():
    # Simulated entries like a real CA ledger
    entries = [
        {"id": 1, "desc": "Operational Cost", "debit": 50000, "credit": 0},
        {"id": 2, "desc": "Client Payment", "debit": 0, "credit": 120000},
        {"id": 3, "desc": "Tax Filing Fee", "debit": 15000, "credit": 0}
    ]
    return jsonify({"ledger_entries": entries, "auditor_signoff": "HASSAN AHMED"})

if __name__ == '__main__':
    app.run(debug=True)