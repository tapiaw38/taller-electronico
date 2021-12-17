# Generated by Django 2.2 on 2021-11-19 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('producto', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=50, verbose_name='número de serie')),
                ('extra', models.CharField(blank=True, max_length=80, null=True, verbose_name='accesorios incluidos')),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('contrasena', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.TextField()),
                ('fechaen', models.DateField(blank=True, null=True, verbose_name='fecha de entrega')),
                ('diagnostico', models.TextField(blank=True, null=True)),
                ('realizar', models.TextField(blank=True, null=True, verbose_name='proceso realizado')),
                ('observacion', models.TextField(blank=True, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('entrega', models.NullBooleanField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created', '-modified'],
            },
        ),
    ]
