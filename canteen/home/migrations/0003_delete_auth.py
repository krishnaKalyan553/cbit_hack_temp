# Generated by Django 4.1.5 on 2023-01-29 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auth_delete_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auth',
        ),
    ]
