# Generated by Django 4.0 on 2021-12-29 16:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_name', models.CharField(max_length=200)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_contact', models.CharField(max_length=20)),
                ('emp_role', models.CharField(max_length=200)),
                ('emp_salary', models.IntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
