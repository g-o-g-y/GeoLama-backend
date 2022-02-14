from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns


class PanoCoordinates(models.Model):
    """Class model containing panorama coordinates"""

    # Fields
    coords_id = models.IntegerField(null=False, primary_key=True)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def return_coords(self):
        return {
            'lon': self.longitude,
            'lat': self.latitude
        }


class Rating(models.Model):
    """Class model containing user's score"""

    # Fields
    # user_id = models.IntegerField(primary_key=True)
    username = models.CharField(null=False, unique=True, primary_key=True, max_length=255)
    points = models.IntegerField(default=0)
    # Metadata
    # class Meta:
    # сортировка
    #     ordering = ["points"]
        # ordering = ["title", "-pubdate"]
    # Methods

    # def get_absolute_url(self):
    #     """ Returns the url to access a particular instance of MyModelName."""
    #     return reverse('users', args=[str(self.user_id)])

    # def __str__(self):
    #     """
    #     String for representing the MyModelName object (in Admin site etc.)
    #     """
    #     return self.user_name
