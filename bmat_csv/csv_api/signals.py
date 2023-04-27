from uuid import uuid4

from csv_api.models import CSVTask
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.text import slugify
import os


@receiver(post_save, sender=CSVTask)
def generate_slug_csv_task(sender, instance, created, **kwargs):
    if created:
        uid = uuid4().hex
        instance.task_id = slugify(f"{instance.id}-{uid}")
        instance.save()
