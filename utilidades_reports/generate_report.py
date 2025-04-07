import json
from jinja2 import Template
from weasyprint import HTML

# Cargar el archivo de salida del SAST
with open('gl-sast-report.json') as f:
    findings = json.load(f).get('vulnerabilities', [])

# Plantilla HTML básica
template_str = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Reporte de SAST</title>
  <style>
    body { font-family: sans-serif; margin: 20px; }
    h1 { color: #003366; }
    .vuln { margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
  </style>
</head>
<body>
  <h1>Reporte de Vulnerabilidades SAST</h1>
  {% for vuln in findings %}
    <div class="vuln">
      <h2>{{ vuln.name }}</h2>
      <p><strong>Severidad:</strong> {{ vuln.severity }}</p>
      <p><strong>Descripción:</strong> {{ vuln.description }}</p>
      <p><strong>Archivo:</strong> {{ vuln.location.file }}</p>
    </div>
  {% else %}
    <p>No se encontraron vulnerabilidades.</p>
  {% endfor %}
</body>
</html>
"""

# Renderizar HTML
html = Template(template_str).render(findings=findings)
with open("report.html", "w") as f:
    f.write(html)

# Convertir a PDF
HTML("report.html").write_pdf("report.pdf")
