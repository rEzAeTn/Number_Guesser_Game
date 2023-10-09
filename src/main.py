from typing import Union

from src.utils.get_start_end import StartEnd
from src.game_logic.hint_generator import provide_hint
from src.game_logic.random_number_generator import generate_random_number
from src.game_logic.scorer import Score
from src.utils.input_validator import validate_input


def main() -> None:
    """
    Main function to run the number guessing game.

    This function generates a random number, takes the user's guess, validates it,
    provides a hint based on the guess, and offers the option to restart the game


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
    You Winner
    Do You Want to Play Again? Y or ...N
    End Game
    """


    while True:

        # Define Range(start, end) of Game Numbers
        print('Define Range of Game Numbers')
        start_end = StartEnd()
        start = start_end.start()
        end = start_end.end()

        # Generate a random number between start and end
        actual_number = generate_random_number(start=start, end=end)

        # Define Score
        score = Score()

        while True:

            # Get and validate the user's guess
            user_guess = validate_input(start=start, end=end)

            # If the user wants to quit the game
            if user_guess == 'Quit':
                print('GoodBye')
                break

            # If the user's guess is not valid (validate_input returned an error message)
            if type(user_guess) == str:
                # Subtract the Penalty from the Score
                decr_score = score.decrement_score(penalty=10)
                print(user_guess)
            else:
                # Provide a hint based on the user's guess
                hint = provide_hint(user_guess=user_guess, actual_number=actual_number)
                # Subtract the Penalty from the Score
                decr_score = score.decrement_score(penalty=5)
                print(hint)

                # If the user guessed correctly(Restart Game)
                if hint == 'You Winner':
                    print(f'Your Score: {decr_score + 5}')
                    restart_game = input('Do You Want to Play Again? Y or ...')
                    if restart_game.upper() == 'Y':
                        break
                    else:
                        print('End Game')


if __name__ == '__main__':
    main()
