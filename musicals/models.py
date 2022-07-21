from django.db import models
from django.contrib.auth.models import AbstractUser


class Musical(models.Model):
    title = models.CharField(max_length=200)
    contributors = models.CharField(max_length=400)
    iswc = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "musicals_musical"


# Creating custom user just incase it can be useful
class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "musicals_user"
