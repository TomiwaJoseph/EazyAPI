from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [          
            'title', 'description',
            'operating_system',
            'processor', 'processor_technology',
            'graphics', 'memory',
            'hard_drive', 'wireless',
            'power_supply', 'battery',           
        ]
        read_only_fields = ['']
        
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     return obj.get_api_url(request=request)