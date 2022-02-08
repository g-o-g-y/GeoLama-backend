from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns


class Users(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    user_id = models.AutoField(max_length=100, null=False, primary_key=True)
    user_name = models.CharField(max_length=100)
    user_points = models.IntegerField(max_length=20)
    user_email = models.EmailField(max_length=100)
    # Metadata
    # class Meta:
    # сортировка
        # ordering = ["-my_field_name"]
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
