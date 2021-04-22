from django.core.management.base import BaseCommand
from apps.countries.models import *
import requests
import os


class Command(BaseCommand):
    country_api_url: str = os.getenv('COUNTRY_API', 'https://restcountries.eu/rest/v2/all')
    city_api_url: str = os.getenv('CITY_API', 'https://countriesnow.space/api/v0.1/countries/cities')
    help = 'Init and update country database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting parse countries...')

        try:
            response = requests.get(self.country_api_url)
            countries_json = response.json()

            for country in countries_json:
                currencies_ids: list = []
                languages_ids: list = []
                cities_ids: list = []
                country_name: str = country.get('name').lower() if country.get('name') else None
                currencies = country.get('currencies')
                languages = country.get('languages')

                # ---------------------
                # Push currencies to DB
                # ---------------------

                if len(currencies) > 0:
                    for country_currency in currencies:
                        currency = Currency.objects.get_or_create(
                            **country_currency
                        )

                        currencies_ids.append(currency[0].id)

                # --------------------
                # Push languages to DB
                # --------------------

                if len(languages) > 0:
                    for lang in languages:
                        language = Language.objects.get_or_create(
                            **lang
                        )

                        languages_ids.append(language[0].id)

                # ------------------
                # Push cities to DB
                # ------------------

                if country_name is not None:
                    data = {
                        'country': country_name
                    }
                    response = requests.post(self.city_api_url, data=data)

                    response_json = response.json()

                    if not response_json['error']:
                        cities_list = response_json.get('data')
                        for country_city in cities_list:
                            city = City.objects.get_or_create(
                                name=country_city
                            )
                            cities_ids.append(city[0].id)

                # --------------------------------------
                # Prepare data for pushing to Country DB
                # --------------------------------------

                filtered_country_data = {
                    key: country[key] for key in country.keys()
                    & {
                        'name',
                        'capital',
                        'population',
                        'nativeName',
                        'numericCode'
                      }
                }

                # print(filtered_country_data.get('name'), ':')
                #
                # print('LANG: ', languages_ids)
                # print('CURR: ', currencies_ids)

                # filtered_country_data['languages'] = languages_ids
                # filtered_country_data['currencies'] = currencies_ids

                # --------------------
                # Push countries to DB
                # --------------------

                saved_country = Country.objects.get_or_create(
                    **filtered_country_data
                )

                # --------------------------------------------
                # If new country, add currencies and languages to country data
                # --------------------------------------------

                if saved_country[1]:
                    saved_country[0].languages.set(languages_ids)
                    saved_country[0].currencies.set(currencies_ids)
                    saved_country[0].cities.set(cities_ids)

            self.stdout.write('Done!')

        except Exception as e:
            print(e)







