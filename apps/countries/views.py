from django.shortcuts import render
from rest_framework import viewsets, views, generics, mixins
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer
import re
# Create your views here.


class CountryViewSet(generics.GenericAPIView):
    cities: list = []
    response: dict = {}

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        cities_str = self.request.GET.get('cities')
        self.cities = cities_str.split(',')
        print(self.cities)
        queryset = self.queryset.filter(cities__name__in=self.cities)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        # serializer.context["cities"] = self.cities

        new_serializer_data = serializer.data

        if len(new_serializer_data) == 0:
            return Response(
                {
                    'error': True,
                    'message': 'Invalid City Name',
                    'request_city': self.cities[0],
                }, 400
            )

        else:
            for country in new_serializer_data:
                for city in country.get('cities'):
                    if city.get('name') in self.cities:
                        self.cities.remove(city.get('name'))
                        country['request_city'] = city.get('name')
                        country['success'] = True

            if len(self.cities) != 0:
                new_serializer_data.append(
                    {
                        'request_city': self.cities[0],
                        'message': 'Invalid City Name',
                        "success": False
                    })

            return Response(
                {
                    'error': False,
                    'data': new_serializer_data
                }
            )


