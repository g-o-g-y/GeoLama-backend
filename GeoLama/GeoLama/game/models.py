from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns


class Raining(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    user_id = models.IntegerField(null=False, primary_key=True)
    user_points = models.IntegerField(default=0)
    # Metadata
    class Meta:
    # сортировка
        ordering = ["user_points"]
        # ordering = ["title", "-pubdate"]
    # Methods

    def get_absolute_url(self):
        """ Returns the url to access a particular instance of MyModelName."""
        return reverse('users', args=[str(self.user_id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.user_name
