# Generated by Django 3.0.8 on 2020-07-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='angkatan',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='student',
            name='nim',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]