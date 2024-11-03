from django.db import models

class MelanomaImage(models.Model):
    image = models.ImageField(upload_to='melanoma_images/')
    is_malignant = models.BooleanField(null=True)
    probability = models.FloatField(null=True)