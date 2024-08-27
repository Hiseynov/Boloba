from rest_framework import serializers
from shop.models import Shop, ProductImage, ProductVersion

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # Обеспечивает возврат полного URL для изображений

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'title']

class ProductVersionSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # Сериализатор для связанных изображений

    class Meta:
        model = ProductVersion
        fields = ['id', 'product', 'color', 'cover_image', 'images']

class ShopSerializer(serializers.ModelSerializer):
    detal_Image = ProductImageSerializer(many=True, read_only=True)  # Изображения продукта
    main_product_version = serializers.SerializerMethodField()  # Главная версия продукта
    product_versions = ProductVersionSerializer(many=True, read_only=True)  # Все версии продукта
    created = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()
    newPrice = serializers.SerializerMethodField()
    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'is_new', 'price', 'endirim','newPrice', 'star',
            'description', 'RewardPoints', 'category', 'manufacturer', 'Availability',
            'detal_Image', 'main_product_version', 'product_versions', 'is_published','created','updated'
        ]

    def get_main_product_version(self, obj):
        # Найти основную версию продукта. Предполагаем, что главная версия - это первая версия.
        main_version = obj.product_versions.first()  # Предполагаем, что главная версия - первая версия
        if main_version:
            return ProductVersionSerializer(main_version).data
        return None
    
    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')

    def get_updated(self, obj):
        return obj.update.strftime('%Y-%m-%d %H:%M:%S')
    
    def get_newPrice(self, obj):
        
        return obj.price * (100 - obj.endirim) / 100

