# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-09 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jongro_Female_30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Female_40',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Female_50',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Female_60',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Male_20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Male_30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Male_40',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Male_50',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongro_Male_60',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Female_20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Female_30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Female_40',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Female_50',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Female_60',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Male_20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Male_30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Male_40',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Male_50',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowon_Male_60',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STD_DD', models.DateField()),
                ('MCT_CAT_CD', models.IntegerField()),
                ('SEX_CD', models.CharField(max_length=1)),
                ('AGE_CD', models.IntegerField()),
                ('USE_CNT', models.IntegerField()),
                ('USE_AMT', models.IntegerField()),
                ('PM10', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
    ]
