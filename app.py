
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, Response
from monitoring.collector import get_system_metrics
from monitoring.alerts import evaluate_alerts
from utils.db import init_db, get_setting, set_setting, list_servers, add_server, delete_server
from utils.reports import build_csv_report, build_pdf_report
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-key'
init_db()

@app.context_processor
def globals_():
    return {'app_name':'EIMS Pro','now':datetime.now()}

@app.route('/')
def index(): return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    metrics=get_system_metrics(); alerts=evaluate_alerts(metrics)
    return render_template('dashboard.html',metrics=metrics,alerts=alerts)

@app.route('/analytics')
def analytics(): return render_template('analytics.html')

@app.route('/api/metrics')
def api_metrics():
    metrics=get_system_metrics()
    return jsonify({'timestamp':datetime.now().isoformat(),'metrics':metrics,'alerts':evaluate_alerts(metrics)})

@app.route('/alerts')
def alerts_page():
    metrics=get_system_metrics(); return render_template('alerts.html',alerts=evaluate_alerts(metrics),metrics=metrics)

@app.route('/servers',methods=['GET','POST'])
def servers():
    if request.method=='POST':
        name=request.form.get('name','').strip(); host=request.form.get('host','').strip(); env=request.form.get('environment','Production')
        if name and host: add_server(name,host,env); flash('Server added.','success')
        else: flash('Server name and host are required.','danger')
        return redirect(url_for('servers'))
    return render_template('servers.html',servers=list_servers())

@app.post('/servers/<int:server_id>/delete')
def delete_server_route(server_id):
    delete_server(server_id); flash('Server removed.','success'); return redirect(url_for('servers'))

@app.route('/reports')
def reports(): return render_template('reports.html')

@app.get('/reports/csv')
def report_csv():
    return Response(build_csv_report(get_system_metrics()),mimetype='text/csv',headers={'Content-Disposition':'attachment; filename=eims_metrics.csv'})

@app.get('/reports/pdf')
def report_pdf():
    return Response(build_pdf_report(get_system_metrics()),mimetype='application/pdf',headers={'Content-Disposition':'attachment; filename=eims_metrics.pdf'})

@app.route('/settings',methods=['GET','POST'])
def settings():
    if request.method=='POST':
        set_setting('refresh_interval',request.form.get('refresh_interval','5')); set_setting('theme',request.form.get('theme','dark')); flash('Settings saved.','success'); return redirect(url_for('settings'))
    return render_template('settings.html',refresh_interval=get_setting('refresh_interval','5'),theme=get_setting('theme','dark'))

if __name__=='__main__': app.run(debug=True,host='127.0.0.1',port=5000)
