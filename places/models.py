from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=255, unique=True),
    )

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    address = models.CharField(_("Address"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=255, null=True, blank=True)
    site = models.CharField(_("Site"), max_length=255, null=True, blank=True)
    registered = models.BooleanField(_("Registered"), default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="places",
        verbose_name=_("User"),
    )
    categories = models.ManyToManyField(
        Category, related_name="places", verbose_name=_("Categories")
    )
    image = models.ImageField(
        _("Image"), upload_to="images", default="images/default.png"
    )

    class Meta:
        verbose_name = _("place")
        verbose_name_plural = _("places")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"pk": self.pk})
