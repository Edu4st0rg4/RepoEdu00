# Generated by Django 4.2.1 on 2023-06-11 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mascotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('marca', models.CharField(blank=True, max_length=50, verbose_name='Marca')),
                ('tipo', models.CharField(blank=True, max_length=50, verbose_name='Tipo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mascotas.categoria', verbose_name='Producto')),
            ],
        ),
        migrations.DeleteModel(
            name='Alimentos',
        ),
    ]
