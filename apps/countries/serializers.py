from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name',
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'name',
            'nativeName',
            'iso639_1',
            'iso639_2'
        ]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'name',
            'code',
            'symbol'
        ]


class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)
    currencies = CurrencySerializer(many=True, read_only=True)
    cities = CitySerializer(many=True, read_only=True)
    # request_city = serializers.SerializerMethodField(read_only=True)
    #
    # def get_request_city(self, obj):
    #     for city in self.context.get("cities"):
    #         print(self.context.get("view"))
    #     return self.context.get("cities")

    class Meta:
        model = Country
        fields = [
            'name',
            'capital',
            'cities',
            'currencies',
            'languages',
            'population',
            'nativeName',
            'numericCode'
        ]


