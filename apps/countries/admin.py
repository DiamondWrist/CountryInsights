from django.contrib import admin
from .models import *
# Register your models here.


class CountryAdmin(admin.ModelAdmin):

    search_fields = [
        'id',
        'name',
        'capital',
        'numericCode',
    ]

    list_display = [
        'id',
        'name',
        'capital',
        'numericCode',
        'nativeName',
        'population',
    ]


class LanguageAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'name',
        'nativeName',
        'iso639_1',
        'iso639_2',
    ]

    list_display = [
        'id',
        'name',
        'nativeName',
        'iso639_1',
        'iso639_2',
    ]


class CurrencyAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'name',
        'code',
    ]

    list_display = [
        'id',
        'name',
        'code',
        'symbol',
    ]


class CityAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'name',
    ]

    list_display = [
        'id',
        'name',
    ]


admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(City, CityAdmin)
