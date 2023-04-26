from django.core.validators import FileExtensionValidator
from django.db import models

from django.utils.timezone import now
from channels.db import database_sync_to_async
import os
from csv_api.utils import GroupSongsPlaysPerDay
from django.core.files.base import ContentFile
import time
# Create your models here.


class CSVTask(models.Model):
    file = models.FileField(
        upload_to="media/csv_files",
        blank=False,
        null=False,
        validators=[FileExtensionValidator(["csv", "txt"])],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_id = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Task: {self.task_id}"

    def convert_csv(self):
        """Converts the file to a CSV file"""
        time.sleep(2)
        new_csv = GroupSongsPlaysPerDay().generate_csv(self.file.path)
        new_csv = ContentFile(new_csv.encode("utf-8"))
        os.remove(self.file.path)
        self.file.save(f"songs-output-{self.task_id}.csv", new_csv)
        self.completed_at = now()
        self.save()

 


    # Models Meta data settings
    class Meta:
        verbose_name = "CSV Task"
        verbose_name_plural = "CSV Tasks"
        ordering = ["-created_at"]
