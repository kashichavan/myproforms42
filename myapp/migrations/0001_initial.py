# Generated by Django 5.0.1 on 2024-02-13 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('designation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('sal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]