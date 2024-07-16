from django.db import models

class add_view(models.Model):
    rest_name = models.CharField(max_length=255)
    rest_spec = models.CharField(max_length=255)
    rest_address = models.CharField(max_length=255)
    rest_website = models.CharField(max_length=255)
    rest_phone = models.IntegerField(max_length=14)