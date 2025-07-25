country = input() # Add country name
visits = int(input()) # Number of visits
cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country_visited, total_visits, list_of_cities):
    new_country = {
      "country": country_visited,
      "visits": total_visits,
      "cities": list_of_cities
    }
    travel_log.append(new_country)

add_new_country(country, visits, cities)
print(travel_log)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")