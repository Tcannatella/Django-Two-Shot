# Generated by Django 5.0 on 2023-12-14 18:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receipt",
            old_name="tac",
            new_name="tax",
        ),
    ]
