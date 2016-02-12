from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone


from .models import ModelsLog


@receiver(post_save)
def log_edit(sender, **kwargs):
    if sender.__name__ == 'ModelsLog':
        return

    action = 'created' if kwargs['created'] else 'updated'
    models_log = ModelsLog(
        model_name=sender.__name__,
        date=timezone.now(),
        action=action
    )
    models_log.save()


@receiver(post_delete)
def log_delete(sender, **kwargs):
    if sender.__name__ == 'ModelsLog':
        return

    models_log = ModelsLog(
        model_name=sender.__name__,
        date=timezone.now(),
        action='deleted'
    )
    models_log.save()
