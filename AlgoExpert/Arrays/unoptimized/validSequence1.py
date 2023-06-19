def isValidSubsequence(array, sequence):
    start_index = 0
    match_index = 0
    while start_index < len(array) and match_index < len(sequence):
        if array[start_index] == sequence[match_index]:
            match_index = match_index + 1
        start_index = start_index + 1
    return match_index == len(sequence)


isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [25])
