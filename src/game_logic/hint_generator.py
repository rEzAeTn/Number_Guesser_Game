def provide_hint(user_guess: int, actual_number: int) -> None:
    """
    This function takes the user's guess and the actual number, and provides a hint.

    hint to the user about whether their guess is more than, less than, or equal to the actual number.

    Parameters
    ----------
    user_guess : int
        The number guessed by the user.
    actual_number : int
        The actual number that the user is trying to guess.

    Returns
    -------
    print(Hint)

    Examples
    --------
    >>> provide_hint(50, 100)
    50 Is Less Than Game Number

    >>> provide_hint(150, 100)
    150 Is More Than Game Number

    >>> provide_hint(100, 100)
    You Winner)
    """

    # If the user's guess is more than the actual number
    if user_guess > actual_number:
        return f'` {user_guess} ` Is More Than Game Number'

    # If the user's guess is less than the actual number
    elif user_guess < actual_number:
        return f'` {user_guess} ` Is Less Than Game Number'

    # If the user's guess is equal to the actual number
    else:
        return 'You Winner'
