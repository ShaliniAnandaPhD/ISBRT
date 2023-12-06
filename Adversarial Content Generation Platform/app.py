from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Placeholder for data to be displayed
    data = {"response_analysis": "Sample Analysis Results"}
    return render_template('dashboard.html', data=data)

@app.route('/report')
def report():
    # Placeholder for a detailed report
    report = "Detailed Analysis Report"
    return render_template('report.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)
