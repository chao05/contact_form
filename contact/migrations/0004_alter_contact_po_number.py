# Generated by Django 4.0.4 on 2022-05-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_client_contact_office_contact_salesperson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='po_number',
            field=models.CharField(max_length=10, verbose_name="销售单号（'7'开头）"),
        ),
    ]
