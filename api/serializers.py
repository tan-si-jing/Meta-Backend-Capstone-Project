from .models import MenuItem
from rest_framework.serializers import ModelSerializer

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only = ['id']