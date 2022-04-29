def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    elif high_index <= low_index:  # caso especial para palavras com 2 letars
        return True
    elif word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
