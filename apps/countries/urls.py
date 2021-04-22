from django.urls import path, include
from .views import CountryViewSet

app_name = 'countries'


urlpatterns = [
    path('country/insight', CountryViewSet.as_view(), name='get-country-insight'),
]
