# persona_generator.py

import random

def create_advanced_persona():
    # Basic demographic attributes
    demographics = {
        "Age": random.randint(18, 80),
        "Gender": random.choice(["Male", "Female", "Non-Binary"]),
        "Location": random.choice(["Urban", "Suburban", "Rural"]),
        "Occupation": random.choice(["Engineer", "Teacher", "Artist", "Healthcare Professional", "Student", "Retired"]),
        "Education Level": random.choice(["High School", "Bachelor's Degree", "Master's Degree", "Doctorate"]),
        "Marital Status": random.choice(["Single", "Married", "Divorced", "Widowed"]),
        "Income Bracket": random.choice(["Low", "Middle", "High"])
    }

    # Psychographic attributes
    psychographics = {
        "Values": random.choice(["Tradition", "Benevolence", "Universalism", "Self-Direction", "Achievement"]),
        "Interests": random.choice(["Sports", "Arts", "Technology", "Travel", "Reading", "Gardening"]),
        "Lifestyle": random.choice(["Active", "Sedentary", "Balanced"]),
        "Personality Type": random.choice(["Extroverted", "Introverted", "Ambivert"]),
        "Hobbies": random.choice(["Photography", "Cooking", "Hiking", "Gaming", "Dancing"]),
        "Spending Habits": random.choice(["Saver", "Spender", "Investor", "Budget-Conscious"])
    }

    # Advanced attributes for deeper persona profiling
    emotional_state = random.choice(["Calm", "Anxious", "Excited", "Sad", "Content", "Frustrated"])
    problem_solving_skill = random.choice(["Analytical", "Creative", "Logical", "Intuitive", "Practical", "Strategic"])
    communication_style = random.choice(["Assertive", "Passive", "Aggressive", "Passive-Aggressive", "Empathetic", "Direct"])

    # Additional attributes to enrich persona
    cultural_background = random.choice(["Asian", "Hispanic", "African", "European", "Middle Eastern", "Native American"])
    health_and_fitness = random.choice(["Fitness Enthusiast", "Health Conscious", "Casually Active", "Sedentary"])
    technology_use = random.choice(["Heavy User", "Moderate User", "Light User", "Non-User"])
    travel_preferences = random.choice(["Frequent Traveler", "Occasional Traveler", "Rarely Travels", "Prefers Staycations"])
    environmental_consciousness = random.choice(["Highly Conscious", "Moderately Conscious", "Indifferent", "Unaware"])

    # Creating the persona dictionary
    persona = {
        "Demographics": demographics,
        "Psychographics": psychographics,
        "Emotional State": emotional_state,
        "Problem Solving Skill": problem_solving_skill,
        "Communication Style": communication_style,
        "Cultural Background": cultural_background,
        "Health and Fitness": health_and_fitness,
        "Technology Use": technology_use,
        "Travel Preferences": travel_preferences,
        "Environmental Consciousness": environmental_consciousness
    }

    return persona

# Example use of the function
if __name__ == "__main__":
    generated_persona = create_advanced_persona()
    print("Generated Persona:", generated_persona)
