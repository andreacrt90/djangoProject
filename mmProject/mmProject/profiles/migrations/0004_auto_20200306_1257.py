# Generated by Django 3.0.3 on 2020-03-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200306_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
    ]