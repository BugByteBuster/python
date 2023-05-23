#Un optimized:
def isValidSubsequence(array, sequence):
    indices = []
    if len(sequence) > len(array):
        return False
    for element in sequence:
        if element in array or array.count(element) == 1:
            indices.append(array.index(element))
        else:
            return False
    if len(set(indices)) == 1:
        return True
    if sorted(indices) != indices or len(set(indices)) < len(indices):
        return False
    return True


"""
    for element in sequence:   >> O(n)
        if element in array or array.count(element) == 1:  >> O(n)
    
    O(n) * O(n) = O(n2) timecomplexity
"""
