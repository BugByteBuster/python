# o(n)
def isPalindrome(string):
    rightIdx = len(string) - 1
    leftIdx = 0

    while leftIdx != rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx = leftIdx + 1
        rightIdx = rightIdx - 1
    return True


# o(n^2)
def isPalindrome2(string):
    reverseString = ""
    for i in reversed(range(len(string))):
        reverseString = reverseString + string[i]
    return reverseString == string
