from django.db import models


class UserHistory(models.Model):
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.message