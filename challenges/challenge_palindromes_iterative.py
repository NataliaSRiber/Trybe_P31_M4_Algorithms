def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    if len(word) <= 2 and word[0] == word[-1]:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome_iterative(word[1:-1])
