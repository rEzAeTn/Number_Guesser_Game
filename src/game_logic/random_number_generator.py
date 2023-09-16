import random
from typing import Union


def generate_random_number(start: int, end: int) -> int:
    """
    Generate a random integer within a given range.

    This function uses the random module to generate a random integer between
    the start and end parameters, inclusive.

    Parameters
    ----------
    start : int
        The lower bound of the range for generating the random number.
    end : int
        The upper bound of the range for generating the random number.

    Returns
    -------
    int
        A random integer within the specified range.

    Examples
    --------
    >>> generate_random_number(1, 10)
    6  # Your output will vary as it's randomly generated
    """
    # Generate Random Integer Number Between Start and End
    random_number = random.randint(start, end)

    return random_number
