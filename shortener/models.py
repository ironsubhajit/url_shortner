from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=20000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return f"<UUID: {self.uuid}>"
