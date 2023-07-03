def isPalindrome(string):
    rightIdx = len(string) - 1
    leftIdx = 0

    while leftIdx != rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx = leftIdx + 1
        rightIdx = rightIdx - 1
    return True
