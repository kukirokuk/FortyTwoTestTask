from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    args = '<model_name model_name ...>'
    help = "Prints to console number of objects in every model of the project."

    def handle(self, *args, **options):
        models_list = [mod for mod in models.get_models()]
        for mod in models_list:
            self.stdout.write('Model %s has %d objects'
                              % (mod.__name__, mod.objects.count()))

            self.stderr.write('error: %s %d'
                              % (mod.__name__, mod.objects.count()))
