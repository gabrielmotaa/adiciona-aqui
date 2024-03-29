# Generated by Django 4.2 on 2023-09-21 03:36

import django.db.models.deletion
import parler.fields
import parler.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("places", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="place",
            options={"verbose_name": "place", "verbose_name_plural": "places"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="name",
        ),
        migrations.AlterField(
            model_name="place",
            name="address",
            field=models.CharField(max_length=255, verbose_name="Address"),
        ),
        migrations.AlterField(
            model_name="place",
            name="categories",
            field=models.ManyToManyField(
                related_name="places", to="places.category", verbose_name="Categories"
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
        ),
        migrations.AlterField(
            model_name="place",
            name="image",
            field=models.ImageField(
                default="images/default.png", upload_to="images", verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="place",
            name="phone",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Phone"
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="registered",
            field=models.BooleanField(default=False, verbose_name="Registered"),
        ),
        migrations.AlterField(
            model_name="place",
            name="site",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Site"
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="places",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.CreateModel(
            name="CategoryTranslation",
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
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="Name"),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="places.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "category Translation",
                "db_table": "places_category_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
