from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('phones', 'Phones'),
        ('laptops', 'Laptops'),
        ('tablets', 'Tablets'),
        ('headphones', 'Headphones'),
        ('speakers', 'Speakers'),
        ('cameras', 'Cameras'),
        ('gaming', 'Gaming'),
        ('smartwatches', 'Smartwatches'),
        ('smarthome', 'Smart Home'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
