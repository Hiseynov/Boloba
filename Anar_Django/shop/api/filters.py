import django_filters
from shop.models import Shop, ProductVersion

class ShopFilter(django_filters.FilterSet):
    # Фильтрация по имени магазина
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    
    # Фильтрация по полям связанных ProductVersion через связь
    color = django_filters.CharFilter(field_name='product_versions__color', lookup_expr='icontains')
    # Фильтрация по полям 'category' и 'manufacturer' в модели Shop, если они являются полями этой модели
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')
    manufacturer = django_filters.CharFilter(field_name='manufacturer', lookup_expr='icontains')

    class Meta:
        model = Shop
        fields = ['name', 'color', 'category', 'manufacturer']

class ProductVersionFilter(django_filters.FilterSet):
    # Фильтрация по цвету продукта
    color = django_filters.CharFilter(field_name='color', lookup_expr='icontains')
    # Добавляем фильтрацию по category и manufacturer, если требуется
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')
    manufacturer = django_filters.CharFilter(field_name='manufacturer', lookup_expr='icontains')

    class Meta:
        model = ProductVersion
        fields = ['color', 'category', 'manufacturer']