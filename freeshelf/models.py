from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse 


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('category-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name 


class Book(models.Model):
    """A typical class defining a model, derived from the Model class."""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length = 200, unique = True)
    date_added = models.DateTimeField(auto_now_add= True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)


    # Metadata
    class Meta:
        ordering = ['-date_added']
        # verbose_name = 'BetterName'

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('book-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

    