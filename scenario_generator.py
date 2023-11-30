# scenario_generator.py

import random

def create_dynamic_scenario():
    base_scenarios = [
        "You are in a city experiencing a blackout. Find a way to navigate and help others.",
        "You are organizing a community event with limited resources. Plan and execute it successfully.",
        "You are a journalist covering a major political event with ethical dilemmas.",
        # ... Add more base scenarios as needed
    ]

    conditional_elements = {
        "time_of_day": random.choice(["day", "night"]),
        "weather": random.choice(["sunny", "rainy", "snowy"]),
        "unexpected_event": random.choice(["transport strike", "network outage", "sudden news"]),
        # ... Add more conditional elements as needed
    }

    scenario = random.choice(base_scenarios)
    for key, value in conditional_elements.items():
        scenario += f" The {key} is {value}."

    return scenario
