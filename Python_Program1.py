import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            self.data = []

    def display_countries_currencies(self):
        if not self.data:
            print("Data not available. Please fetch data first.")
            return
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    def countries_with_currency(self, currency_name):
        if not self.data:
            print("Data not available. Please fetch data first.")
            return
        countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_info in currencies.values():
                if currency_info.get('name', '').lower() == currency_name.lower():
                    countries.append(country.get('name', {}).get('common', 'N/A'))
        return countries

    def display_countries_with_dollar(self):
        countries = self.countries_with_currency('dollar')
        print(f"Countries using Dollar: {', '.join(countries) if countries else 'None'}")

    def display_countries_with_euro(self):
        countries = self.countries_with_currency('euro')
        print(f"Countries using Euro: {', '.join(countries) if countries else 'None'}")

# URL for fetching country data
url = "https://restcountries.com/v3.1/all"

# Creating an instance of CountryData
country_data = CountryData(url)

# Fetching data from the URL
country_data.fetch_data()

# Displaying countries and their currencies
country_data.display_countries_currencies()

# Displaying countries with Dollar as currency
country_data.display_countries_with_dollar()

# Displaying countries with Euro as currency
country_data.display_countries_with_euro()

