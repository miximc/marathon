# Generated by Django 4.1.4 on 2022-12-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sporsmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Иванан', max_length=1024)),
                ('last_name', models.CharField(default='Иванов', max_length=1024)),
                ('father_name', models.CharField(default='Иванович', max_length=1024)),
                ('birthday', models.DateField()),
                ('weight', models.IntegerField(default=170)),
                ('growth', models.IntegerField(default=80)),
                ('male', models.BooleanField(default=True)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
