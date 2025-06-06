# Generated by Django 5.1.3 on 2024-11-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("esqueceu_senha", "0002_delete_email_paciente"),
    ]

    operations = [
        migrations.CreateModel(
            name="PasswordRecovery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("recovery_code", models.CharField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("expires_at", models.DateTimeField()),
            ],
        ),
    ]
