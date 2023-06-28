# method - 1  O(n)
def isValidSubsequence(array, sequence):
    seqIdx = 0
    arrIdx = 0
    while seqIdx <= len(sequence) and arrIdx < len(array):
        if sequence[seqIdx] == array[arrIdx]:
            seqIdx = seqIdx + 1
        if seqIdx == len(sequence):
            return True
        arrIdx = arrIdx + 1
    return False


# method -2 O(n)
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for ele in array:
        if ele == sequence[seqIdx]:
            seqIdx = seqIdx + 1
        if seqIdx == len(sequence):
            return True
    return False
