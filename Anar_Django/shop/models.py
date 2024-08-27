from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Anar_Django.utils.base import BaseModel

class Shop(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name', help_text="max simvol 100")
    is_new = models.BooleanField(default=False, verbose_name="Is it a new product?")
    price = models.PositiveIntegerField(verbose_name='Product Price')
    endirim = models.IntegerField(null=True, blank=True, default=None, verbose_name='Product Discount')
    star = models.DecimalField(
        max_digits=3, decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name='Product Rating',
        help_text="minimum (0.0) maximum (10.0)"
    )
    description = models.TextField(verbose_name='Product Description')
    RewardPoints = models.IntegerField(verbose_name='Reward Points')
    Availability = models.CharField(max_length=200, verbose_name='Product Availability')
    is_published = models.BooleanField(default=False)
    category = models.CharField(max_length=255, verbose_name='Product Category')
    manufacturer = models.CharField(max_length=255, verbose_name='Manufacturer')
    main_version = models.OneToOneField(
        'ProductVersion',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='main_product',
        verbose_name='Main Product Version'
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Product {self.name}'

class ProductImage(BaseModel):
    image = models.ImageField(upload_to='product_version_img')
    title = models.CharField(max_length=255, verbose_name='Title', help_text='Image description')

    def __str__(self):
        return self.title

class ProductVersion(BaseModel):
    product = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='product_versions')
    color = models.CharField(max_length=255, verbose_name='Color')
    cover_image = models.ImageField(upload_to='product_version_img')
    images = models.ManyToManyField(ProductImage, related_name='product_versions_img', blank=True)
    
    # Adding hover image
    imageHover = models.ImageField(
        upload_to='product_version_img', 
        verbose_name='Hover Image',
        help_text='Add hover image for the product version',
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Product Version'
        verbose_name_plural = 'Product Versions'

    def __str__(self):
        return f"{self.product.name} - {self.color}"
