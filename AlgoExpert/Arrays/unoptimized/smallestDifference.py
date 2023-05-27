#UnOptimized
def smallestDifference(arrayOne, arrayTwo):
    absolute_difference = {}
    for i in range(len(arrayOne)):
      for j in range(len(arrayTwo)):
          absolute_distance = abs(arrayTwo[j] - arrayOne[i])
          absolute_difference[absolute_distance] = [arrayOne[i], arrayTwo[j]]
    sorted_dictionary = dict(sorted(absolute_difference.items()))
    return (list(sorted_dictionary.values())[0])