def isValidSubsequence(array, sequence):
    count = 0
    for i in array:
        if (
            i in sequence
            and array.index(i) >= sequence.index(i)
            and count < len(sequence)
        ):
            count = count + 1

    if count == len(sequence):
        return True
    return False


isValidSubsequence([1, 1, 1, 1, 1], [1, 1, 1])
