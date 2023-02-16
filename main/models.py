from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import os
# Create your models here.


class Exames(models.Model):
    title = models.CharField(max_length=50)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    exame_pdf = models.FileField(upload_to='exames')

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return os.path.basename(self.exame_pdf.name)

