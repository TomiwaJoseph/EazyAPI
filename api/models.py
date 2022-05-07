from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse as api_reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.ForeignKey("Category", on_delete=models.CASCADE,
        related_name="product_category", null=True)
    operating_system = models.CharField(max_length=50)
    processor = models.CharField(max_length=150)
    processor_technology = models.CharField(max_length=100)
    graphics = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    hard_drive = models.CharField(max_length=100)
    wireless = models.CharField(max_length=100)
    power_supply = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to="products")
    real_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    slug = models.SlugField(max_length=100)
    other_product_images = models.ManyToManyField("ProductImages")

    def __str__(self):
        return self.title
    
    def get_stripe_price(self):
        return int(self.discount_price) * 100

    def get_absolute_url(self):
        return reverse('view_product', args=[self.slug])

    def image_tag(self):
        return mark_safe("<img src='{}' height='30'/>".format(self.main_image.url))

    image_tag.short_description = "Image"
    

class Category(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'


class ProductImages(models.Model):
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE,
        related_name="product_images", null=True)
    # title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/sub_images")

    def __str__(self):
        return "image of {}".format(self.product_id)
    
    class Meta:
        verbose_name = 'Product Images'
        verbose_name_plural = 'Product Images'

