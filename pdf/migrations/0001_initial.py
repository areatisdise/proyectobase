# Generated by Django 5.0.1 on 2024-01-26 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrofact', models.CharField(max_length=40)),
                ('fechaEmis', models.DateField(auto_now_add=True)),
                ('nomCli', models.CharField(max_length=200)),
                ('rucCli', models.CharField(max_length=40)),
                ('dirRecep', models.CharField(max_length=200)),
                ('dirCli', models.CharField(max_length=200)),
                ('tipmon', models.CharField(max_length=200)),
                ('observacion', models.CharField(max_length=600)),
                ('formaPago', models.CharField(max_length=600)),
                ('guiaRemitente', models.CharField(max_length=600)),
                ('importetotalletras', models.CharField(max_length=200)),
                ('wopergrat', models.CharField(max_length=100)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('anticipos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuentos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valorventa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iscfact', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igvfact', models.DecimalField(decimal_places=2, max_digits=10)),
                ('icbperfact', models.DecimalField(decimal_places=2, max_digits=10)),
                ('otroscargos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('otrostributos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montoredondeo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('importetotal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantProd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('undProd', models.CharField(max_length=40)),
                ('codProd', models.CharField(max_length=40)),
                ('codCliProd', models.CharField(max_length=40)),
                ('descProd', models.CharField(max_length=100)),
                ('puProd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('icbperProd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('factura', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pdf.factura')),
            ],
        ),
    ]
