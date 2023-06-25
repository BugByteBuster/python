def arrayOfProducts(array):
    result_array = [1] * len(array)  # Initialize result_array with 1s

    product = 1
    for i in range(len(array)):
        result_array[i] *= product  # Product of elements to the left
        product *= array[i]

    product = 1
    for i in range(len(array) - 1, -1, -1):
        result_array[i] *= product  # Product of elements to the right
        product *= array[i]

    return result_array
