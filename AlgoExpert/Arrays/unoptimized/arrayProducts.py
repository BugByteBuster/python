def arrayOfProducts(array):
    init = 0
    result_array = []
    while init < len(array):  #O(n)
        init += 1
        product = 1
        left_array = array[0:init-1]
        right_array = array[init:]
        product_list = left_array + right_array
        for i in product_list:    #O(n)
            product *= i
        result_array.append(product)
    return result_array       #O(n^2)