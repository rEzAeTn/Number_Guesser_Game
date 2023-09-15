import random


def validate_input(user_guess):
    start_number = 1
    end_number = 100

    # Negative Number Is Valid
    if user_guess.startswith('-') and user_guess[1:].isdigit():
        return True

    # Check that the input is a integer
    if not user_guess.isdigit():
        print("Invalid Input, Please Input Integer Number")
        return False


    # Checking that the input is within the specified range
    user_guess_int = int(user_guess)
    if user_guess_int < start_number or user_guess_int > end_number:
        print(f'*{user_guess_int}* Is Out Of Range, Your Guess Should be Between {start_number} To {end_number}')
        return False

    # Input Number Is Valid
    return True


def main():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        user_guess = input("Guess a  Number")

        # Calculate Score
        score = max(score, 0)
        if score == 0 :
            print(f'Your Score is: {score}')
            print('GAME OVER')
            break

        # Quit Game
        if user_guess.upper() == 'Q':
            print("END GAME")
            break

        # Check Validate Input
        if not validate_input(user_guess):
            print(f'OOPs -10 Score :(')
            score -= 10
            continue

        # convert input: str to int
        user_guess_int = int(user_guess)

        # Hint: Guess Number is Less Than OR More Than
        if user_guess_int > rand_num:
            print(f'OOPs -5 Score :(')
            score -= 5
            print(f'{user_guess_int} Is More Than Game Number')
        elif user_guess_int < rand_num:
            print(f'OOPs -5 Score :(')
            score -= 5
            print(f'{user_guess_int} Is Less Than Game Number')
        else:
            print(f'Your Score: {score}')
            print('congratulations, You Guessed The Correct Number :)')
            break



if __name__ == '__main__':
    main()
