from django.db import models

# Create your models here.
class Employee(models.Model):
    code = models.CharField(primary_key = True, max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.name, self.code)