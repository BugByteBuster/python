# lifted and optimized
def isMonotonic(array):
    increasing = decreasing = True
    for i in range(len(array) - 1):
        increasing = increasing and array[i] <= array[i + 1]
        decreasing = decreasing and array[i] >= array[i + 1]
    return increasing or decreasing
