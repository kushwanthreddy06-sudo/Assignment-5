travel_places = {

    "beach": ["Goa", "Maldives", "Bali"],

    "hill": ["Ooty", "Manali", "Munnar"],

    "historical": ["Delhi", "Agra", "Hampi"]
}

budget_plan = {

    "low": "Bus + Budget Hotel",

    "medium": "Train + Standard Hotel",

    "high": "Flight + Luxury Hotel"
}

def recommend_trip(preference, budget):

    print("\nRecommended Places:")

    for place in travel_places[preference]:
        print(place)

    print("\nTravel Plan:")
    print(budget_plan[budget])


# User Input
preference = input("Enter Preference: ")
budget = input("Enter Budget: ")

recommend_trip(preference, budget)
