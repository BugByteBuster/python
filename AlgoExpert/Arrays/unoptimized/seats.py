def bestSeat(seats):
    possible_places = []


    for i in range(1, len(seats)-1):
        if seats[i] == 0:
            possible_places.append(i)
    
    print(possible_places)
    
    if len(possible_places) > 2:
        i = 0
        while i < len(possible_places)-1:
            if seats[i] == 0 and seats[i - 1] == 0 and seats[i + 1] == 0:
                print(possible_places)
                possible_places.remove(i)
            i+=1
    elif len(possible_places) == 0:
        return -1
    else:
        return min(possible_places)




print(bestSeat(seats = [ 1, 0, 0, 0, 0, 0, 0, 1]))