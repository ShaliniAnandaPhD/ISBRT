# simulation_controller.py
# Manages the lifecycle of simulation scenarios

import threading
import time

class SimulationController:
    def __init__(self):
        self.simulation_thread = None
        self.simulation_active = False
        self.simulation_paused = False

    def simulation_task(self):
        """ The main task or process of the simulation """
        while self.simulation_active:
            if self.simulation_paused:
                continue
            # Replace the line below with the actual simulation work
            print("Simulation running...")
            time.sleep(1)  # Simulate some work being done

    def start_simulation(self):
        """ Start the simulation """
        if not self.simulation_thread or not self.simulation_thread.is_alive():
            self.simulation_active = True
            self.simulation_paused = False
            self.simulation_thread = threading.Thread(target=self.simulation_task)
            self.simulation_thread.start()
            print("Simulation started.")

    def pause_simulation(self):
        """ Pause the simulation """
        if self.simulation_active and not self.simulation_paused:
            self.simulation_paused = True
            print("Simulation paused.")

    def resume_simulation(self):
        """ Resume the simulation """
        if self.simulation_active and self.simulation_paused:
            self.simulation_paused = False
            print("Simulation resumed.")

    def stop_simulation(self):
        """ Stop the simulation """
        if self.simulation_active:
            self.simulation_active = False
            self.simulation_thread.join()
            print("Simulation stopped.")

# Example usage
if __name__ == '__main__':
    controller = SimulationController()
    
    # Start the simulation
    controller.start_simulation()
    time.sleep(5)
    
    # Pause the simulation
    controller.pause_simulation()
    time.sleep(2)

    # Resume the simulation
    controller.resume_simulation()
    time.sleep(3)

    # Stop the simulation
    controller.stop_simulation()
