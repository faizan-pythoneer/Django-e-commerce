# Generated by Django 4.2.4 on 2024-10-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='men', max_length=10),
        ),
    ]
