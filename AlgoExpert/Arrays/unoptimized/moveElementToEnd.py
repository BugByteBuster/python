#Un-optimized: O(n) time complexity
def moveElementToEnd(array, toMove):
    move_end_array = []
    occurrence = array.count(toMove)
    if occurrence == 0:
        return array
    for i in array:
        if i != toMove:
            move_end_array.append(i)
    for i in range(occurrence):
        move_end_array.append(toMove)
    
    return move_end_array