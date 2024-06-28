import requests
from collections import Counter

# API endpoint
api_url = "https://api.openbrewerydb.org/breweries"

# States to query
states = ["Alaska", "Maine", "New York"]

def get_breweries_by_state(state):
    response = requests.get(f"{api_url}?by_state={state}&per_page=200")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {state}")
        return []

# Data collection
breweries_by_state = {state: get_breweries_by_state(state) for state in states}

# Task 1: List the names of all breweries
breweries_names = {state: [brewery['name'] for brewery in breweries] for state, breweries in breweries_by_state.items()}

# Task 2: Count the number of breweries in each state
breweries_count = {state: len(breweries) for state, breweries in breweries_by_state.items()}

# Task 3: Count the number of types of breweries in individual cities
brewery_types_by_city = {state: Counter([(brewery['city'], brewery['brewery_type']) for brewery in breweries]) for state, breweries in breweries_by_state.items()}

# Task 4: Count and list breweries with websites
breweries_with_websites = {state: [brewery['website_url'] for brewery in breweries if brewery['website_url']] for state, breweries in breweries_by_state.items()}
breweries_with_websites_count = {state: len(breweries) for state, breweries in breweries_with_websites.items()}

# Print results
print("Breweries Names by State:")
for state, names in breweries_names.items():
    print(f"{state}: {names}")

print("\nCount of Breweries by State:")
for state, count in breweries_count.items():
    print(f"{state}: {count}")

print("\nBrewery Types by City:")
for state, types in brewery_types_by_city.items():
    print(f"{state}: {types}")

print("\nBreweries with Websites:")
for state, websites in breweries_with_websites.items():
    print(f"{state}: {websites}")

print("\nCount of Breweries with Websites by State:")
for state, count in breweries_with_websites_count.items():
    print(f"{state}: {count}")

