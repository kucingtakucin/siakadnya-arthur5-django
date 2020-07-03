# Generated by Django 3.0.8 on 2020-07-03 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=255)),
                ('prodi', models.CharField(choices=[('IF', 'Teknik Informatika'), ('EL', 'Teknik Elektro'), ('MS', 'Teknik Mesin'), ('TI', 'Teknik Industri'), ('LI', 'Teknik Lingkungan')], default='IF', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matkul', models.CharField(max_length=30)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]