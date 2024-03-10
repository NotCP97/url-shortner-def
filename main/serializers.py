from main.models import ShortURL
from rest_framework import serializers
from main.services import generate_short_url


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'short_url', 'created_at', 'updated_at']
        read_only_fields = ['short_url']
        extra_kwargs = {
            'url': {'required': True}
        }

    def create(self, validated_data):
        
        validated_data.update({'short_url': generate_short_url(validated_data["url"])})
        
        return ShortURL.objects.create(**validated_data)



        
        