from django.db.models import Count
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ShopSerializer, ProductVersionSerializer
from .filters import ShopFilter, ProductVersionFilter
from shop.models import Shop, ProductVersion

class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter  # Используем ShopFilter для Shop

class ShopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ProductVersionListCreateView(generics.ListCreateAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductVersionFilter  # Используем ProductVersionFilter для ProductVersion
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data
        
        # Check if the response is a dictionary and contains 'results'
        if isinstance(data, dict) and 'results' in data:
            response_data = {
                'results': data['results'],
                'color_counts': self.get_color_counts(),
                'manufacturer_counts': self.get_manufacturer_counts(),
                'category_counts': self.get_category_counts(),
            }
        else:
            response_data = {
                'results': data,
                'color_counts': self.get_color_counts(),
                # Optional: 'manufacturer_counts': self.get_manufacturer_counts(),
                # Optional: 'category_counts': self.get_category_counts(),
            }

        return Response(response_data)

    def get_color_counts(self):
        color_counts = ProductVersion.objects.values('color').annotate(count=Count('color')).order_by('color')
        return {item['color']: item['count'] for item in color_counts}

    def get_manufacturer_counts(self):
        manufacturer_counts = ProductVersion.objects.values('product__manufacturer').annotate(count=Count('product__manufacturer')).order_by('product__manufacturer')
        return {item['product__manufacturer']: item['count'] for item in manufacturer_counts}

    def get_category_counts(self):
        category_counts = ProductVersion.objects.values('product__category').annotate(count=Count('product__category')).order_by('product__category')
        return {item['product__category']: item['count'] for item in category_counts}
