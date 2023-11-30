# content_generator.py
# Dynamically generates content for scenarios and personas

import random
import string

class ContentGenerator:
    def __init__(self):
        # Initialize with any necessary data or parameters
        self.scenario_templates = ["Scenario A: {}", "Scenario B: {}", "Scenario C: {}"]
        self.persona_attributes = {
            "Names": ["Alex", "Jordan", "Taylor", "Morgan", "Casey"],
            "Age": range(18, 70),
            "Occupations": ["Engineer", "Artist", "Teacher", "Doctor", "Writer"],
            # ... add more attributes as necessary
        }

    def generate_random_string(self, length=10):
        """ Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def generate_scenario_content(self):
        """ Generate scenario content """
        chosen_template = random.choice(self.scenario_templates)
        scenario_content = chosen_template.format(self.generate_random_string())
        return scenario_content

    def generate_persona_content(self):
        """ Generate persona content """
        persona = {attr: random.choice(values) if isinstance(values, list) else random.choice(list(values))
                   for attr, values in self.persona_attributes.items()}
        return persona

    # Additional content generation methods as needed

# Example usage
if __name__ == '__main__':
    generator = ContentGenerator()
    
    # Generate scenario content
    scenario = generator.generate_scenario_content()
    print("Generated Scenario:", scenario)
    
    # Generate persona content
    persona = generator.generate_persona_content()
    print("Generated Persona:", persona)
