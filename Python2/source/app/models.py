from django.db import models
from .conf import SpecificationChoices, PropertyTypeChoices

# Create your models here.
class Property(models.Model):
    '''
    Model for properties
    '''
    description = models.CharField(max_length=50)
    photos = models.ImageField(upload_to='images', null=True, blank=True)
    cost = models.FloatField()
    specifictions = models.PositiveSmallIntegerField(
        choices=SpecificationChoices.SPECIFICATION_CHOICES, default=SpecificationChoices.STRUCTURE)
    location = models.CharField(max_length=50)
    property_type = models.PositiveIntegerField(
        choices=PropertyTypeChoices.PROPERTY_TYPE_CHOICES, default=PropertyTypeChoices.APARTMENT)
    is_active = models.BooleanField(default=True)

    class Meta(object):
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return str(self.pk)
    
