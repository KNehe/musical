from django.db import models
from django.contrib.auth.models import AbstractUser


class Musical(models.Model):
    title = models.CharField(max_length=200)
    contributors = models.ManyToManyField(
        "musicals.Contributor",
        related_name="musicals",
    )
    iswc = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "musicals_musical"

    def __str__(self) -> str:
        return self.title


class Contributor(models.Model):
    # ideally should be first_name, last_name, other_names
    # but do not know the limit of the number of names yet
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "musicals_contributor"


# Creating custom user just incase it can be useful
class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "musicals_user"
