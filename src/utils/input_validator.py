from typing import Union


def validate_input(start: int, end: int) -> Union[int, str]:
    """
    This function it takes an input from the user, checks if it's an integer and falls within the given range.

    If the input is valid, it returns the input as an integer.
    If the input is not valid, it provides an appropriate error message.

    Parameters
    ----------
    start_num : int
        The start of the valid range for guessing.
    end_num : int
        The end of the valid range for guessing.

    Returns
    -------
    Union[int, str]
        If the user's guess is valid, returns the guess as an integer.
        If the user's guess is not valid, returns an error message as a string.

    Examples
    --------
    >>> validate_input(1, 100)
    Guess a Number, For EXIT Enter Q --> 50
    return 50
    """

    user_guess = input('Guess a Number, For Quit Enter ` Q `: ')

    # Quit Game
    if user_guess.upper() == 'Q':
        return "Quit"

    # Check That The Input Is a Integer
    if not (user_guess.isdigit() or (user_guess.startswith('-') and user_guess[1:].isdigit())):
        return "Invalid Input, Please Input Integer Number"

    # Convert Input to Integer
    user_guess_int = int(user_guess)

    # Checking That The Input is Within the Specified Range
    if user_guess_int < start or user_guess_int > end:
        return f'` {user_guess_int} ` Is Out Of Range, Your Guess Should be Between `{start}` To `{end}`'

    # Input Number Is Valid
    return user_guess_int
