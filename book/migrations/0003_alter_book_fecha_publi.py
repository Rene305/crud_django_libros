# Generated by Django 5.0.2 on 2024-02-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_fecha_publi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='fecha_publi',
            field=models.DateField(null=True, verbose_name='dd/mm/aa'),
        ),
    ]