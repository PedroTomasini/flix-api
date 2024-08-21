from rest_framework import serializers
from django.db.models import Avg
from.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    # Soma média das estrelas em Reviews de cada filme
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None


    # Validar POST
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior que 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo deve ter menos que 200 caracteres')
        return value
    