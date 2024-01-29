from django.db import models

# Create your models here.
class Factura(models.Model):
    nrofact = models.CharField(max_length=40)
    fechaEmis = models.DateField(auto_now_add=True)
    nomCli = models.CharField(max_length=200)
    rucCli = models.CharField(max_length=40)
    dirRecep = models.CharField(max_length=200)
    dirCli = models.CharField(max_length=200)
    tipmon = models.CharField(max_length=200)
    observacion = models.CharField(max_length=600)
    formaPago = models.CharField(max_length=600)
    guiaRemitente = models.CharField(max_length=600)  # Corregido aquí
    importetotalletras = models.CharField(max_length=200)
    wopergrat = models.CharField(max_length=100)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    anticipos = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    descuentos = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    valorventa = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    iscfact = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    igvfact = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    icbperfact = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    otroscargos = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    otrostributos = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    montoredondeo = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    importetotal = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades

    def __str__(self):
        return str(self.nrofact)

class Producto(models.Model):
    cantProd = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    undProd = models.CharField(max_length=40)
    codProd = models.CharField(max_length=40)
    codCliProd = models.CharField(max_length=40)
    descProd = models.CharField(max_length=100)
    puProd = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    icbperProd = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, default=1)  # Ajusta según tus necesidades

    def __str__(self):
        return str(self.codProd)