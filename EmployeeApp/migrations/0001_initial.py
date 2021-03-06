# Generated by Django 4.0 on 2022-01-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departements',
            fields=[
                ('DepartementId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartementName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=255)),
                ('Departement', models.CharField(max_length=255)),
                ('DateOfJoint', models.DateField()),
                ('PhotoFilName', models.CharField(max_length=255)),
            ],
        ),
    ]
