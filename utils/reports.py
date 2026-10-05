import csv,io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def build_csv_report(data):
    o=io.StringIO(); w=csv.writer(o); w.writerow(['Metric','Value']); [w.writerow([k,v]) for k,v in data.items()]; return o.getvalue()
def build_pdf_report(data):
    b=io.BytesIO(); p=canvas.Canvas(b,pagesize=A4); p.setTitle('EIMS Pro Report'); p.setFont('Helvetica-Bold',18); p.drawString(50,800,'EIMS Pro - Infrastructure Report'); y=770; p.setFont('Helvetica',10)
    for k,v in data.items():
        p.drawString(60,y,f'{k}: {v}'); y-=18
        if y<60: p.showPage(); y=800
    p.save(); b.seek(0); return b.read()
