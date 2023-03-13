from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length =50)
    address=models.CharField(max_length =50)
    phone=models.IntegerField()
    def __str__(self):
        return self.name
