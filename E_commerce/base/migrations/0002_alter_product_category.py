# Generated by Django 5.1.5 on 2025-01-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('EB', 'Earbuds'), ('SW', 'Smart Watch'), ('MS', 'Mouse'), ('SB', 'Sound Box'), ('RT', 'Router'), ('SF', 'Stand Fan'), ('PT', 'Printer'), ('KB', 'Keyboard'), ('HP', 'Headphone'), ('PB', 'Power Bank')], max_length=2),
        ),
    ]
