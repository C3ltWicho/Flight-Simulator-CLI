

# Flight Simulator CLI

## Overview
The **Flight Simulator CLI** is a command-line interface that simulates flight operations. It allows users to interact with the simulator by providing commands to modify parameters like altitude, speed, and temperature. Users can also run predefined scenarios to simulate different flight conditions.

## Features
- **Increase/Decrease Simulator Parameters**: Adjust altitude, speed, and temperature using commands like `increase altitude 100` or `decrease speed 50`.
- **Predefined Scenarios**: Run predefined flight scenarios such as **Takeoff** or **Descent** by entering commands like `run scenario Takeoff`.
- **Exit the Simulator**: Exit the simulator by typing `exit`.

## Setup

### Prerequisites
Ensure you have Python 3.x installed.

You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/flight-simulator-cli.git
   cd flight-simulator-cli
   ```

2. Install any required dependencies (if applicable, e.g., logging):

   ```bash
   pip install -r requirements.txt
   ```

### Running the Simulator

To start the simulator, simply run the `simulator_clit.py` file:

```bash
python simulator_clit.py
```

Once the simulator is running, you can enter commands to interact with it.

## Command Syntax

- **Increase Parameter**:
  ```
  increase [parameter] [value]
  ```
  Example:
  ```bash
  increase altitude 100
  ```

- **Decrease Parameter**:
  ```
  decrease [parameter] [value]
  ```
  Example:
  ```bash
  decrease speed 50
  ```

- **Run Scenario**:
  To run a predefined scenario, use:
  ```
  run scenario [scenario_name]
  ```
  Example:
  ```bash
  run scenario Takeoff
  ```

- **Exit**:
  To exit the simulator, use the `exit` command:
  ```bash
  exit
  ```

## Available Scenarios
- **Takeoff**: Simulates the aircraft taking off.
- **Descent**: Simulates the aircraft descending.

### Example Usage

1. **Increase Altitude**:
   ```bash
   increase altitude 100
   ```

2. **Run Scenario**:
   ```bash
   run scenario Takeoff
   ```

3. **Exit**:
   ```bash
   exit
   ```

## Logging
The simulator includes logging functionality to track commands and events. Logs are saved at the `INFO` level and can be customized based on your needs.

## Contributions
Feel free to fork this repository, make changes, and submit pull requests. Contributions are welcome!

## License
This project is open-source and available under the [MIT License](LICENSE).
