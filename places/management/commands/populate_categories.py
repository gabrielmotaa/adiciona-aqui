from django.core.management.base import BaseCommand
from places.models import Category

CATEGORIES = [
    'Açougue',
    'Bar',
    'Cafeteria',
    'Casa noturna',
    'Cozinha solidária',
    'Padaria',
    'Sorveteria',
    'Supermercado',
    'Loja',
    'Armazém',
    'Farmácia',
    'Floricultura',
    'Livraria',
    'Joalheria',
    'Tabacaria',
    'Banco',
    'Barbearia',
    'Cabelereiro',
    'Estacionamento',
    'Imobiliária',
    'Manicure',
    'Oficina',
    'Posto de combustivel',
    'Salão de beleza',
    'Cuidados pessoais',
    'Lavanderia',
    'Hotel',
    'Motel',
    'Academia',
    'Clube',
    'Parque',
    'Museu',
    'Igreja',
    'Repartição pública',
    'Autoescola',
    'Escola',
    'Universidade',
]

class Command(BaseCommand):
    help = 'Popula o banco de dados com as categorias do Google'

    def handle(self, *args, **options):
        if Category.objects.all().count() > 0:
            self.stdout.write(
                self.style.WARNING('Comando já foi rodado, pulando')
            )
            return

        Category.objects.bulk_create([
            Category(name=category) for category in CATEGORIES
        ])

        self.stdout.write(
            self.style.SUCCESS('Categorias populadas no banco')
        )
