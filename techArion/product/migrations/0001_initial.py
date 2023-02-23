# Generated by Django 4.1.7 on 2023-02-23 11:40

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductMain",
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
                ("title", models.TextField(max_length=50)),
                ("description", models.TextField(max_length=200)),
                (
                    "unique_id",
                    models.CharField(
                        default=product.models.generate_product_id,
                        max_length=6,
                        unique=True,
                    ),
                ),
                ("price", models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("image", models.ImageField(upload_to="product_images/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.productmain",
                    ),
                ),
            ],
        ),
    ]
