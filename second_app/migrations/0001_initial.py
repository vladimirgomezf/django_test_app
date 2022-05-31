# Generated by Django 4.0.4 on 2022-05-31 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('ci', models.CharField(max_length=11, verbose_name='Carné de Identidad')),
                ('dir', models.CharField(blank=True, max_length=75, null=True, verbose_name='Dirección')),
                ('tel', models.CharField(blank=True, max_length=30, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('dir', models.CharField(blank=True, max_length=75, null=True, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='second_app.persona')),
                ('year', models.CharField(max_length=20, verbose_name='Año Académico')),
                ('prom', models.FloatField(default=0, verbose_name='Promedio')),
                ('ayudante', models.BooleanField(default=False, verbose_name='Es alumno ayudante?')),
            ],
            bases=('second_app.persona',),
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('responsable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='second_app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='second_app.persona')),
                ('depto', models.CharField(max_length=20, verbose_name='Departamento')),
                ('evaluacion', models.CharField(choices=[('B', 'Bien'), ('R', 'Regular'), ('M', 'Mal')], max_length=20, verbose_name='Evaluación')),
                ('asignatura', models.CharField(max_length=20, verbose_name='Asignatura')),
                ('carrera', models.ManyToManyField(to='second_app.carrera')),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.universidad')),
            ],
            bases=('second_app.persona',),
        ),
    ]