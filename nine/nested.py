#nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a dictionary
tavel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting list and dictionary in a dictionary
travel_log = {
    "France" : {"cities_visited": ["Paris", "Lion", "Dijon"], "total_visits": 12},
    "Italy": {"favorite_cities": ["Venice","Vicenza","Rome"], "total_visits": 15}
}

# nesting a dictionary inside of the list
travel_log2 = [
    {"country": "France",
    "cities_visited": ["Paris", "Lion", "Dijon"],
     "total_visits": 12
    },
    {"country": "Italy",
    "cities_visited": ["Venice","Vicenza","Rome"],
     "total_visits": 15
    }
]