from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Url(models.Model):
    link = models.CharField(max_length=20000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return f"<UUID: {self.uuid}>"


class UserUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=20000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return f"<{self.user} Url>"
