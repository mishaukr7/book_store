from django.db import models
from django.utils import timezone
from isbn_field import ISBNField
# Create your models here.
from simple_history.models import HistoricalRecords


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)

    class Meta:
        db_table = 'author'
        ordering = ['last_name', 'first_name']


class Book(models.Model):
    isbn = ISBNField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(default=timezone.now)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
