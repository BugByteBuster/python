# o(n)
def caesarCipherEncryptor(string, key):
    comparator = "abcdefghijklmnopqrstuvwxyz"
    result_string = ""
    for literal in string:
        index = comparator.find(literal)
        if index + key > 25:
            new_index = (index + key) % 26
        else:
            new_index = index + key
        result_string = result_string + comparator[new_index]
    return result_string
