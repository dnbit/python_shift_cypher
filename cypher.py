shift = 3
initial_ascii_value = 64
ascii_range = 26


def cypher(input):
    if input is None:
        raise TypeError("Invalid input: None")
    return __generate_string(input)


def decypher(input):
    if input is None:
        raise TypeError("Invalid input: None")
    return __generate_string(input, False)


def __generate_string(input, cypher=True):
    output = ''
    cache = {}

    for character in input:
        new_character = cache.get(character, None)
        if not new_character:
            number = ord(character) - initial_ascii_value
            if number < 0 or number > ascii_range:
                raise ValueError(f'Invalid input: {character} not allowed')

            number = __shift_number(number, cypher)

            new_character = chr(number + initial_ascii_value)
            cache[character] = new_character

        output += new_character

    return output


def __shift_number(number, cypher):
    if cypher:
        number += shift
        if number > ascii_range:
            number -= ascii_range
    else:
        number -= shift
        if number < 1:
            number += ascii_range

    return number
