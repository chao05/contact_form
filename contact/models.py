from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    po_number = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.email
