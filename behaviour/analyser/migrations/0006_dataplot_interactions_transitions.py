# Generated by Django 4.0.4 on 2022-04-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyser', '0005_rawdata_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='data_plots/')),
            ],
        ),
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='interactions/')),
            ],
        ),
        migrations.CreateModel(
            name='Transitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='transitions/')),
            ],
        ),
    ]
