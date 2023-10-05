# Generated by Django 4.2.5 on 2023-10-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('mother_Fname', models.CharField(max_length=50)),
                ('mother_Lname', models.CharField(max_length=50)),
                ('father_Fname', models.CharField(max_length=50)),
                ('father_Lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('fee', models.FloatField()),
                ('fee_status', models.CharField(max_length=10)),
                ('student_status', models.CharField(max_length=20)),
                ('allergies', models.CharField(max_length=255)),
            ],
        ),
    ]
