#lifted and optimized
def isMonotonic(array):
    a = True
    b = True
    for i in range(len(array) - 1):
        a = a and array[i] < array[i + 1]
        b = b and array[i] > array[i + 1]
    return a or b