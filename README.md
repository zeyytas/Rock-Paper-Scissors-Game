# Rock-Paper-Scissors Game

A  Rock-Paper-Scissors game implemented in Python. This game allows a player to compete against the computer in multiple rounds, with the results displayed after each round.

## Features
- You can play several rounds against the computer.
- It validates player input and handles errors.
- It shows the results of each round, including ties, wins for the player, and wins for the computer.

## Requirements
- **Python 3.6** or higher is required because this project uses features like f-strings and type hints that are not available in earlier versions.

## How to Run the Game

1. **Unzip the downloaded file and navigate to the project folder.**


2. **Create a virtual environment in the current folder.**

   *_Although not strictly necessary, creating a virtual environment is recommended to avoid dependency conflicts._

   ```bash
   python3 -m venv env
   ```
  
3. **Activate the virtual environment.**

   - On macOS and Linux
   ```bash
   source env/bin/activate
   ```

   - On Windows
   ```bash
   .\env\Scripts\activate
   ```

4. **Run the game.**:

   Run the game using the command line:
   ```bash
   python -m rps_game
   ```

5. **Run the tests**:

   To run tests, execute:
   ```bash
   python -m test_rps_game
   ```
