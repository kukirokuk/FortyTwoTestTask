from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone


from .models import ModelsLog


@receiver(post_save)
def log_edit(sender, **kwargs):
    models_log = ModelsLog()
    models_log.model_name = sender.__name__
    models_log.date = timezone.now()

    if sender.__name__ == 'SavedRequest' or sender.__name__ == 'Contact':
        if kwargs['created']:
            models_log.action = "created"
            models_log.save()
        else:
            models_log.action = "updated"
            models_log.save()


@receiver(post_delete)
def log_delete(sender, **kwargs):
    models_log = ModelsLog()
    models_log.model_name = sender.__name__
    models_log.date = timezone.now()

    if sender.__name__ == 'SavedRequest' or sender.__name__ == 'Contact':
        models_log.action = "deleted"
        models_log.save()
