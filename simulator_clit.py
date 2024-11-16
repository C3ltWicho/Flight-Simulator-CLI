from test_simulation import FlightSimulator
from scenarios import Scenarios
from Logger import setup_logging

logger = setup_logging("INFO")



def process_command(simulator, command):
    parts = command.split()
    if len(parts) == 3:
        action, parameter, value = parts[0], parts[1], parts[2]
        try:
            value = int(value)
            logger.info(f"Executing command: {command}")
            if action == "increase":
                if parameter == "altitude":
                    simulator.increase_altitude(value)
                elif parameter == "speed":
                    simulator.increase_speed(value)
                elif parameter == "temperature":
                    simulator.increase_temperature(value)
            elif action == "decrease":
                if parameter == "altitude":
                    simulator.decrease_altitude(value)
                elif parameter == "speed":
                    simulator.decrease_speed(value)
            else:
                logger.warning(f"Invalid command format: {command}")
                print("Invalid command format.")
            logger.info(f"Simulator state: {simulator.get_state()}")
            print(simulator.get_state())
        except ValueError:
            logger.error(f"Invalid value for command: {command}")
            print("Please enter a valid integer for the amount.")
    else:
        logger.warning(f"Unrecognized command: {command}")
        print("Command not recognized. Use format: 'increase altitude 100' or 'decrease speed 50'.")

def main():
    simulator = FlightSimulator()
    print("Welcome to the Flight Simulator CLI")
    print("Type commands like 'increase altitude 100', 'decrease speed 50', or 'exit' to quit.\n")
    print("Or type commands to run Scenarios like 'run scenario  \n")

    # Debugging: Print loaded scenarios
    print("Available Scenarios:", list(Scenarios.keys()))

    def run_scenario(simulator, scenario_name):
        print(f"\nRunning scenario: {scenario_name}\n")
        for command in Scenarios[scenario_name]:
            print(f"Executing: {command}")
            process_command(simulator, command)
        print(f"\nScenario '{scenario_name}' complete.\n")

    while True:
        command = input("Enter command: ").strip().lower()
        if command == "exit":
            print("Exiting the simulator.")
            break
        elif command.startswith("run scenario"):
            _, scenario_name = command.split("run scenario ", 1)
            scenario_name = scenario_name.strip().capitalize()
            
            # Debugging: Check if scenario name matches
            print(f"User entered scenario name: '{scenario_name}'")
            if scenario_name in Scenarios:
                run_scenario(simulator, scenario_name)
            else:
                print("Scenario not found.")
        else:
            process_command(simulator, command)

if __name__ == "__main__":
    main()
