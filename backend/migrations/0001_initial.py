# Generated by Django 3.2.8 on 2021-11-24 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPVUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('officephone', models.CharField(blank=True, max_length=100)),
                ('cellphone', models.CharField(blank=True, max_length=100)),
                ('prefix', models.CharField(max_length=10)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now_add=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('clientname', models.CharField(max_length=100)),
                ('clienttype', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificateNumber', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('reportNumber', models.IntegerField(blank=True)),
                ('clientID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.client')),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='spvuser',
            name='clientID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.client'),
        ),
    ]
