'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # this function will traverse trough the list from left to right
    # if the number we are looking at is greater than 0 then it moves 
    # to the left of the list
    # other wise it 
    for i in arr:
        if i == 0:
            idx = arr.index(i)
            arr.append(arr.pop(idx))

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")