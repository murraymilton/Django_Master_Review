from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestseller = models.BooleanField(default=False)
    #Optimize Search/Query in the db by setting db_index=True
    slug = models.SlugField(default="", null=False, db_index=True) #automate url slug --> title-1


    # def get_absolute_url(self):
    #     return reverse("book_details", args=[self.id])

    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug])

# Will override the save method and use the title model to dynamically change each URL local.../book-life-1
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"