from django.db import models
from djmoney.models.fields import MoneyField


class Book(models.Model):
    title = models.CharField(max_length=2**8)
    author = models.CharField(max_length=2**8)
    isbn = models.CharField(max_length=13)
    price = MoneyField(max_digits=2**4, decimal_places=2)
    description = models.TextField(blank=True)

    def __repr__(self):
        return "{0} by {1}".format(self.title, self.author)
    
    def __str__(self):
        return "{0} by {1}".format(self.title, self.author)

class Library(models.Model):
    name = models.CharField(max_length=2**8)
    books = models.ManyToManyField(Book)

    def __repr__(self):
        return self.name

    class Meta:
         verbose_name_plural = "Libraries"
