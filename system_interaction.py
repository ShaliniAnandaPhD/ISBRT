# system_interaction.py

def interact_with_system(persona, scenario, system_api):
    print(f"Persona: {persona}")
    print(f"Scenario: {scenario}")

    while True:
        user_input = input("Enter your action: ")
        if user_input.lower() == "exit":
            break

        system_input = {
            "persona": persona,
            "scenario": scenario,
            "user_action": user_input
        }

        # Placeholder for system interaction
        system_response = system_api.send(system_input)

        print(f"System Response: {system_response}")
