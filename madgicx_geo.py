import requests
import sys
import re

# --------------------
# Get args
# --------------------

api_url = 'https://protected-harbor-94258.herokuapp.com/api/country/insight'
# api_url = 'http://localhost:8000/api/country/insight' # LOCAL API URL

cities_input: str = " ".join(sys.argv[1:])
# print(cities_input)

cities: str
params: dict = {'cities': {}}
cities = cities_input.replace(', ', ',').title()


# --------------------
# Parse helpers
# --------------------


def parse_currency(currencies: dict) -> str:
    currency_string: str = ''
    for currency in currencies:
        currency_string += (
            f" - Name: {currency.get('name')}\n"
            f" - Code: {currency.get('code')}\n"
            f" - Symbol: {currency.get('symbol')}\n\n"
        )

    return currency_string


def parse_language(languages: dict) -> str:
    language_string = ''
    for language in languages:
        language_string += (
            f" - Name: {language.get('name')}\n"
            f" - Native Name: {language.get('nativeName')}\n"
            f" - ISO-639-1: {language.get('iso639_1')}\n"
            f" - ISO-639-2: {language.get('iso639_2')}\n\n"
        )

    return language_string


def parse_cities(cities_dict: dict) -> str:
    cities_string = ''
    for city in cities_dict:
        if len(cities_string) == 0:
            cities_string += (
                f"{city.get('name')}"
            )
        else:
            cities_string += (
                f",{city.get('name')}"
            )

    return cities_string


def parse_fail(resp: dict) -> str:
    return (
        f"\nRequest City: {resp.get('request_city')}\n"
        f"-------------------------------\n"
        f"Message: {resp.get('message')}\n"
    )


# --------------------
# Regex to check special characters
# --------------------


def special_match(strg, search=re.compile(r'[^a-zA-Z,\s]').search):
    return not bool(search(strg))


# ------------------------------
# Try to make GET Request to API
# ------------------------------

try:
    if special_match(cities):
        # params['cities'] = {'name': city for city in cities.split(',')}
        # print(params)
        params = {
            'cities': cities
        }

        response = requests.get(api_url, params=params)

        response_json = response.json()

        if not response_json['error']:
            insights = response_json.get('data')
            for insight in insights:
                if insight['success']:
                    print(
                        f"\nRequest City: {insight.get('request_city')}\n"
                        f"-------------------------------\n"
                        f"Country: {insight.get('name')}\n"
                        f"Native Name: {insight.get('nativeName')}\n"
                        f"Numeric Code: {insight.get('numericCode')}\n"
                        f"Population: {insight.get('population')} people\n"
                        f"Capital: {insight.get('capital')}\n\n"
                        f"Language(-es): \n{parse_language(insight.get('languages'))}"
                        f"Currency(-ies): \n{parse_currency(insight.get('currencies'))}"
                        f"Cities: \n{parse_cities(insight.get('cities'))}\n"
                    )
                else:
                    print(
                        parse_fail(insight)
                    )

        else:
            print(
                parse_fail(response_json)
            )

    else:
        raise ValueError(
            'Invalid Input (numbers or special characters)'
        )


except Exception as e:
    print(e)

