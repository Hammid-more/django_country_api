from django.db import models

class Citizen(models.Model):
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    home_town = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)  # e.g., Male, Female, Other

    def __str__(self):
        return f"{self.first_name} ({self.home_town})"
