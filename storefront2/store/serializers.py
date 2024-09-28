from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    
    products_count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'inventory', 'unit_price', 'price_with_tax', 'collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source="unit_price")
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # Collection model has __str__ method, so it can return a string
    # collection = serializers.StringRelatedField()
    # Nested objects
    # collection = CollectionSerializer()
    # if we want to generate a HTTP link
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name = 'collection-detail'
    # )
    def calculate_tax(self, product: Product):
        return product.unit_price*Decimal(1.1)
    
    # if we need to add extra data validations when desrializing
    # we can re-define this method which is already implemented in ModelSerializer
    # def validate(self, data):
    #     if "password" not in data:
    #         return serializers.ValidationError('Bad post')
    #     if not data['password']:
    #         return serializers.ValidationError('Bad post')
    #     return data