from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=254)

    def __str__(self):
        return 'Informações de Contato'
