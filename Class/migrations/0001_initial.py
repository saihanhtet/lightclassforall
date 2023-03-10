# Generated by Django 4.1.4 on 2022-12-17 12:02

import Class.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'COURSE',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'SUBJECT',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_id', models.CharField(max_length=10, unique=True)),
                ('status', models.CharField(choices=[('understudies', 'understudies'), ('complete', 'complete'), ('resign', 'resign')], default='understudies', max_length=100)),
                ('student', Class.models.NameField(max_length=50, null=True)),
                ('guardian', Class.models.NameField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('guardian_ph', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Class.course')),
                ('subjects', models.ManyToManyField(to='Class.subject')),
            ],
            options={
                'db_table': 'STUDENT',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_id', models.CharField(max_length=10, unique=True)),
                ('student', Class.models.NameField(max_length=50, null=True)),
                ('guardian', Class.models.NameField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Class.course')),
                ('subjects', models.ManyToManyField(to='Class.subject')),
            ],
            options={
                'db_table': 'QUERY',
            },
        ),
        migrations.CreateModel(
            name='filterstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('understudies', 'understudies'), ('complete', 'complete'), ('resign', 'resign')], default='understudies', max_length=100)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Class.course')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Class.student')),
            ],
            options={
                'db_table': 'FILTERSTUDENT',
            },
        ),
    ]
