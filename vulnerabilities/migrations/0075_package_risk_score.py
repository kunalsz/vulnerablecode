# Generated by Django 4.2.16 on 2024-10-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vulnerabilities", "0074_update_pysec_advisory_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="risk_score",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Risk score between 0.00 and 10.00, where higher values indicate greater vulnerability risk for the package.",
                max_digits=4,
                null=True,
            ),
        ),
    ]
