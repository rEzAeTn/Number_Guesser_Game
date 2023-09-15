from src.game_logic.hint_generator import provide_hint
from src.game_logic.random_number_generator import generate_random_number
from src.utils.input_validator import validate_input


def main():
    actual_number = generate_random_number(start=1, end=100)
    print(actual_number)

    while True:
        user_guess = validate_input(start=1, end=100)

        # Quit Game
        if user_guess == 'Quit':
            print('GoodBye')
            break

        if type(user_guess) == str:
            print(user_guess)
        else:
            hint = provide_hint(user_guess=user_guess, actual_number=actual_number)
            print(hint)

        if hint == 'You Winner':
            restart_game = input('Do You Want to Play Again? Y or ...')
            if restart_game.upper() == 'Y':
                print('Start Game Again')
                actual_number = generate_random_number(start=1, end=100)
                print(actual_number)
            else:
                print('End Game')
                break


if __name__ == '__main__':
    main()