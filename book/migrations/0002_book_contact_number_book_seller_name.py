# Generated by Django 4.0 on 2021-12-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='contact_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='seller_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
