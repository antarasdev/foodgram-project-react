import json

from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from recipes.models import Ingredient


class Command(BaseCommand):
    help = _('Загрузить ингредиенты')

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(_('Загрузка ингредиентов')))
        with open('ingredients.json', encoding='utf-8') as file:
            ingredients = json.loads(file.read())
            for ingredient in ingredients:
                Ingredient.objects.get_or_create(**ingredient)

        self.stdout.write(self.style.SUCCESS(_('Ингредиенты загружены')))
