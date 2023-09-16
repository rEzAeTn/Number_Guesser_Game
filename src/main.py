from typing import Union

from src.game_logic.hint_generator import provide_hint
from src.game_logic.random_number_generator import generate_random_number
from src.utils.input_validator import validate_input


def main() -> None:
    """
    Main function to run the number guessing game.

    This function generates a random number, takes the user's guess, validates it,
    provides a hint based on the guess, and offers the option to restart the game
    once the correct number is guessed.

    Returns
    -------
    None

    Examples
    --------
    >>> main()
    Guess a Number, For EXIT Enter Q50
    50 Is Less Than Game Number
    Guess a Number, For EXIT Enter Q75
    75 Is More Than Game Number
    Guess a Number, For EXIT Enter Q60
    You Winner)
    Do You Want to Play Again? Y or ...N
    End Game
    """

    # Generate a random number between start and end
    actual_number = generate_random_number(start=1, end=100)

    while True:
        # Get and validate the user's guess
        user_guess = validate_input(start=1, end=100)

        # If the user wants to quit the game
        if user_guess == 'Quit':
            print('GoodBye')
            break

        # If the user's guess is not valid (validate_input returned an error message)
        if type(user_guess) == str:
            print(user_guess)
        else:
            # Provide a hint based on the user's guess
            hint = provide_hint(user_guess=user_guess, actual_number=actual_number)
            print(hint)

            # If the user guessed correctly(Restart Game)
            if hint == 'You Winner':
                restart_game = input('Do You Want to Play Again? Y or ...')
                if restart_game.upper() == 'Y':
                    print('Start Game Again')
                    # Generate a new random number between start and end
                    actual_number = generate_random_number(start=1, end=100)
                else:
                    print('End Game')
                    break


if __name__ == '__main__':
    main()
