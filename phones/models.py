from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
