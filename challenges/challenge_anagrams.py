def sort_string(array):
    array = list(array)
    for i in range(len(array)):
        current_value = array[i]
        current_position = i

        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1

        array[current_position] = current_value
    return array


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    if len(first_string) != len(second_string):
        return False
    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_first_string = sort_string(first_string)
    sorted_second_string = sort_string(second_string)

    return sorted_first_string == sorted_second_string
    



