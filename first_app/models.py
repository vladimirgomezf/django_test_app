from django.db import models


class Address(models.Model):
    street = models.CharField("Street", max_length=250)
    city = models.CharField("City", max_length=50)
    state = models.CharField("State", max_length=50)
    zip = models.CharField("Postal Code", max_length=6)
    country = models.CharField("Country", max_length=50, default="Cuba")

    def __str__(self) -> str:
        return f"{self.street}, {self.city}."
