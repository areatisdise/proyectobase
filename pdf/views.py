
import os

#wkhtmltopdf
from django.http import HttpResponse
from django.shortcuts import render
from .models import Factura, Producto
from django.template.loader import render_to_string
from django.conf import settings
import tempfile
import subprocess
#pip install more-itertools
from more_itertools import chunked

#djangorestframework
from django.http.response import JsonResponse


# Create your views here.
def facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'pdf/facturas.html', {
        'facturas': facturas
    })

def table(request):
    return render(request, 'tables.html')

def generar_pdf(request, id):
    factura = Factura.objects.get(id=id)
    productos = Producto.objects.filter(factura_id=id)
    hojas = list(chunked(productos, 53))

    datos = {
        'factura': factura,
        'productos': productos,
        'hojas': hojas
    }

    # Renderizar el contenido HTML utilizando la plantilla y los datos
    html_template = 'pdf/pdftemplate.html'
    html = render_to_string(html_template, datos)

    # Crear un archivo temporal para el HTML
    temp_html = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    temp_html.write(html.encode('utf-8'))
    temp_html.close()

    # Configuración para el PDF
    output_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    output_pdf.close()

    # Ejecutar wkhtmltopdf para convertir HTML a PDF
    subprocess.run([settings.WKHTMLTOPDF_PATH, temp_html.name, output_pdf.name])

    # Leer el contenido del PDF generado
    with open(output_pdf.name, 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    # Responder con el PDF
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=facturasdise.pdf'

    # Eliminar archivos temporales
    os.unlink(temp_html.name)
    os.unlink(output_pdf.name)

    return response

#django rest framework???
def list_facturas(request):
    facturas = list(Factura.objects.values())
    return JsonResponse(facturas, safe=False)

