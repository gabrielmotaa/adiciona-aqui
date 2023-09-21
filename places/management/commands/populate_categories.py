from django.core.management.base import BaseCommand
from places.models import Category


CATEGORIES_PT_BR = [
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

CATEGORIES_EN = [
    "Butcher's",
    'Pub',
    'Coffee shop',
    'Nightclub',
    'Solidarity Kitchen',
    'Bakery',
    'Ice-cream parlor',
    'Supermarket',
    'Store',
    'Storage',
    'Pharmacy',
    'Floriculture',
    'Bookstore',
    'Jewelry',
    'Tobacconist',
    'Bank',
    'Barbershop',
    'Hairdresser',
    'Parking',
    'Real estate',
    'Manicure',
    'Gym',
    'Fuel station',
    'Beauty salon',
    'Personal cares',
    'Laundry',
    'Hotel',
    'Motel',
    'Academy',
    'Club',
    'Park',
    'Museum',
    'Church',
    'Public repartition',
    'Driving school',
    'School',
    'University',
]

class Command(BaseCommand):
    help = 'Popula o banco de dados com as categorias do Google'

    def handle(self, *args, **options):
        if Category.objects.all().count() > 0:
            self.stdout.write(
                self.style.WARNING('Comando já foi rodado, pulando')
            )
            return

        for name_pt_br, name_en in zip(CATEGORIES_PT_BR, CATEGORIES_EN):
            category = Category()

            category.set_current_language('pt-br')
            category.name = name_pt_br

            if name_pt_br != name_en:
                # se os nomes forem iguais vai ter um erro de unique constraint,
                # django-parler não aceita a mesma string em idiomas diferentes.
                category.set_current_language('en')
                category.name = name_en

            category.save()

        self.stdout.write(
            self.style.SUCCESS('Categorias populadas no banco')
        )
