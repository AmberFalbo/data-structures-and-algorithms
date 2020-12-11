def insert_shift_array(n, array):
    """This is a function

    Args:
        n ([integer]): [a number]
        array ([integers]): [list]]

    Returns:
        [array]: [new list with added number in the middle]
    """

    if not len(array) % 2:
        array.insert(round(len(array)/2), n)
        return array
    else:
        array.insert(int(len(array)/2 + 1), n)
        return array
