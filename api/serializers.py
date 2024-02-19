from .models import MenuItem, Booking
from rest_framework.serializers import ModelSerializer

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only = ['id']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"