from django.db import models
from tastypie.resources import ModelResource
from Vid.models import Movie

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'vid'
  
    