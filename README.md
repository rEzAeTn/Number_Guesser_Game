# Number Guesser Game Project

## Description
This project is a simple and fun Number Guesser Game written in Python. The game generates a random number  between `Start` and `End`, and the user is prompted to guess this number. For each incorrect guess, the user receives a hint and their score is reduced.

## Directory Structure

```
number_guesser/
|-- src/
| |-- main.py
| |-- game_logic/
| | |-- init.py
| | |-- random_number_generator.py
| | |-- hint_generator.py
| | |-- scorer.py
| |-- utils/
| | |-- get_start_end.py
| | |-- input_validator.py
|-- README.md
|-- requirements.txt
```

## Modules

- `src/main.py`: The main entry point of the game. It handles the game loop, user input, and display.
- `src/game_logic/`: Contains the core game logic.
  - `random_number_generator.py`: Generates a random number.
  - `hint_generator.py`: Provides hints based on the user's guess.
  - `scorer.py`: Manages the scoring system.
- `src/utils/`: Contains utility functions.
  - `input_validator.py`: Validates user input.
  - `get_start_end.py`: Define Range of Game Numbers

## How To Run
- Clone the repository to your local machine.
- Open your command line and navigate to the main project directory.
- Run `pip install -r requirements.txt` to install necessary dependencies.
- Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
- Run `python main.py` to start the game.
- Follow the on-screen prompts to play the game.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
