import os
from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# --- DATABASE HELPER ---
def query_db(query, args=(), one=False):
    conn = sqlite3.connect('Audit_Master.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# --- ROUTES ---
@app.route('/')
def index():
    # Dashboard stats nikalna
    stats = {
        "total_assets": 5000000,
        "liabilities": 1200000,
        "tax_due": 45000,
        "risk": "Low"
    }
    return render_template('index.html', stats=stats)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    # AI EXTRACTION SIMULATION (CA Job #1: Bookkeeping)
    # Asli AI yahan Invoice se Amount aur Vendor nikalega
    sample_amount = 15000.0
    vendor = "Hassan Supplies Co."
    
    conn = sqlite3.connect('Audit_Master.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO ledger (date, account_name, category, debit, description) VALUES (?, ?, ?, ?, ?)",
                ('2026-04-29', vendor, 'Purchase', sample_amount, 'Auto-extracted from ' + file.filename))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Success! AI extracted RS {sample_amount} from {file.filename} and updated Ledger."})

if __name__ == '__main__':
    app.run(debug=True)