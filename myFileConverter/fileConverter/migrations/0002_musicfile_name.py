# Generated by Django 4.0.5 on 2022-08-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileConverter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicfile',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
