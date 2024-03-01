# Generated by Django 5.0.1 on 2024-02-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_medios_pago_options_alter_productos_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas_frecuentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.AlterModelOptions(
            name='sucursales',
            options={'ordering': ['ciudad'], 'verbose_name': 'Sucursal', 'verbose_name_plural': 'Sucursales'},
        ),
    ]
