# Generated by Django 4.1.11 on 2023-10-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0004_userprofile_age_userprofile_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="id_proof",
            field=models.CharField(
                blank=True,
                choices=[
                    ("aadharcard", "Aadhar Card"),
                    ("pancard", "PAN Card"),
                    ("other", "Other"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]