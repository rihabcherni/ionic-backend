from rest_framework import serializers
from products.models import Category,Post, Product, ProductVariant, Review, SubCategory, Wishlist 
from django.db.models import Sum

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    image_product = ProductImagesSerializer(many=True, read_only=True)
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='subcategory.category.name')
    subcategory_name = serializers.ReadOnlyField(source='subcategory.name')
    seller_name = serializers.SerializerMethodField()
    total_ratings = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    variants = ProductVariantSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_seller_name(self, obj):
        if obj.seller:
            return f"{obj.seller.first_name} {obj.seller.last_name}"
        return None

    def get_total_reviews(self, obj):
        total_reviews = obj.reviews.count()
        return total_reviews or 0

    def get_total_ratings(self, obj):
        total_ratings = Review.objects.filter(product=obj).aggregate(Sum('rating'))['rating__sum'] 
        return total_ratings or 0

class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'products']