# Generated by Django 3.0.1 on 2020-01-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200101_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exames',
            name='exame_pdf',
            field=models.FileField(upload_to='main/static/'),
        ),
    ]