"""
Garden Advice App

Provides seasonal and plant-specific gardening advice.
The user enters a season and a plant type, and the program
prints the relevant advice.
"""

# Advice for each season, stored in a dictionary.
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

# Advice for each plant type, stored in a dictionary.
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_season_advice(season):
    """Return the gardening advice for the given season."""
    return SEASON_ADVICE.get(season, "No advice for this season.\n")


def get_plant_advice(plant_type):
    """Return the gardening advice for the given plant type."""
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def main():
    """Get user input, generate the advice and print it."""
    # Get the season and plant type from the user so the app is interactive.
    season = input("Enter the season (e.g. summer or winter): ").strip().lower()
    plant_type = input("Enter the plant type (e.g. flower or vegetable): ").strip().lower()

    # Combine the season advice and the plant advice.
    advice = get_season_advice(season) + get_plant_advice(plant_type)

    # Print the generated advice.
    print(advice)


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Recommend plants based on the entered season.
