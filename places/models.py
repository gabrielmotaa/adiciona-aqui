from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Nome', max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class Place(models.Model):
    name = models.CharField('Nome', max_length=255)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    address = models.CharField('Endereço', max_length=255)
    phone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    site = models.CharField('Site', max_length=255, null=True, blank=True)
    registered = models.BooleanField('Registrado', default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='places', verbose_name='Usuário')
    categories = models.ManyToManyField(Category, related_name='places', verbose_name='Categorias')
    image = models.ImageField(upload_to='images', default='images/default.png', verbose_name='Imagem')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place_detail', kwargs={'pk': self.pk})
