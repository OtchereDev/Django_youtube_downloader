from django.db import models


class FileSystem(models.Model):
    output_file=models.FileField()