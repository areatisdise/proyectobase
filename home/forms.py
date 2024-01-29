from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from .models import Producto

class RUCForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=255, required=False)
    tipoDocumento = forms.CharField(label='Tipo de Documento', max_length=10, required=False)
    numeroDocumento = forms.CharField(label='Número de Documento', max_length=20, required=False)
    estado = forms.CharField(label='Estado', max_length=50, required=False)
    condicion = forms.CharField(label='Condición', max_length=50, required=False)
    direccion = forms.CharField(label='Dirección', max_length=255, required=False)
    ubigeo = forms.CharField(label='Ubigeo', max_length=10, required=False)
    viaTipo = forms.CharField(label='Vía Tipo', max_length=50, required=False)
    viaNombre = forms.CharField(label='Vía Nombre', max_length=255, required=False)
    zonaCodigo = forms.CharField(label='Zona Código', max_length=10, required=False)
    zonaTipo = forms.CharField(label='Zona Tipo', max_length=50, required=False)
    numero = forms.CharField(label='Número', max_length=10, required=False)
    interior = forms.CharField(label='Interior', max_length=10, required=False)
    lote = forms.CharField(label='Lote', max_length=10, required=False)
    dpto = forms.CharField(label='Departamento', max_length=10, required=False)
    manzana = forms.CharField(label='Manzana', max_length=10, required=False)
    kilometro = forms.CharField(label='Kilómetro', max_length=10, required=False)
    distrito = forms.CharField(label='Distrito', max_length=50, required=False)
    provincia = forms.CharField(label='Provincia', max_length=50, required=False)
    departamento = forms.CharField(label='Departamento', max_length=50, required=False)

    def __init__(self, *args, **kwargs):
        super(RUCForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Lista de campos
        campos = [field_name for field_name, _ in self.fields.items()]
        orden_de_grupos = [['numero', 'interior'], ['lote', 'dpto'], ['kilometro', 'distrito']]

        # Ajustar el orden de campos
        nuevo_orden_de_campos = self.ajustar_orden_de_campos(campos, orden_de_grupos)

        # Generar el diseño del formulario con el nuevo orden de campos
        self.helper.layout = self.generar_layout(nuevo_orden_de_campos)

    def eliminar_elementos_adyacentes(self, lista, elemento):
        indice = lista.index(elemento)
        if indice == 0:
            lista.pop(indice + 1)
        elif indice == len(lista) - 1:
            lista.pop(indice - 1)
        else:
            lista.pop(indice + 1)

    def ajustar_orden_de_campos(self, campos, orden_de_grupos):
        nuevo_orden = campos.copy()

        for grupo in orden_de_grupos:
            if grupo in nuevo_orden:
                nuevo_orden.remove(grupo)

            pos = -1
            for elemento in grupo:
                if elemento in nuevo_orden:
                    pos = max(pos, nuevo_orden.index(elemento))

            if pos >= 0:
                nuevo_orden.insert(pos, grupo)
            else:
                nuevo_orden.append(grupo)

        for grupo in orden_de_grupos:
            self.eliminar_elementos_adyacentes(nuevo_orden, grupo)

        return nuevo_orden

    def generar_layout(self, orden_de_campos):
        layout = Layout()
        current_row = []

        for field_name in orden_de_campos:
            if isinstance(field_name, list):
                row_layout = Div(css_class='row')
                for subfield_name in field_name:
                    row_layout.append(
                        Div(
                            Field(subfield_name, css_class='form-control col-6',
                                  placeholder=self.fields[subfield_name].label),
                            css_class='col-6'
                        )
                    )
                layout.append(row_layout)
            else:
                layout.append(
                    Div(
                        Field(field_name, css_class='form-control col-12', placeholder=self.fields[field_name].label),
                        css_class='row'
                    )
                )

        return layout


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.DecimalField()




