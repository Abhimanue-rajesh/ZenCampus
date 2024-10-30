# Generated by Django 5.1.2 on 2024-10-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MAL', 'Male'), ('FEM', 'Female'), ('OTH', 'Other')], max_length=3, null=True),
        ),
    ]