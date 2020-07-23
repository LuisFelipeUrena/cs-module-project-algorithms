'''
Input: a List of integers
Returns: a List of integers
'''
    # for each value at the list exclude that given value
    # then get the product of all the elements in the list
    # and replace that value with the product of all the numbers
    # rinse and repeat
    # first we need to know how to exclude the value of that list and then at that index location
    # inserting the product of the list
    # [0,3,5,6,3,5] the whole list
    # [0]excluded index [3,5,6,3,5] remaining of the list
    # [1350] product of all numbers
    # put the list back together but with the excluded value replaced [1350,3,5,6,3,5]
    # OR: 
    # grabbbing the original list, create a new empty list
    # loop over the original list and exclude the given value from it
    # getting the product of the segregated list
    #append that to the empty list in order
    # then overwrite the old list with new list with the given numbers


def product_of_all_other_numbers(arr):
    product = []
    result = 1
    for i in arr:
        idx = arr.index(i)
        arr.pop(idx)
        for x in arr:
            result = result * x
            product.append(result)
        arr.insert(idx, i)    
    return product


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
