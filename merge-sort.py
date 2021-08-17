'''
SIMILAR
-------------------------------------------------------------------------
https://leetcode.com/problems/merge-sorted-array/

PROMPT
-------------------------------------------------------------------------
Write a Merge Sort algo to sort the array [3, 4, 5, 1, 2, 6]
'''

arr = [1, 4, 2, 3, 5, 10, 8, 6, 4]

def mergeSort(list):
    if len(list) == 1:
        return list

    mid = len(list) // 2

    left_side = list[:mid]
    right_side = list[mid:]

    # print(left_side)
    # print(right_side)

    left_side = mergeSort(left_side)
    right_side = mergeSort(right_side)

    # make a new array to merge left and right into
    new_arr = []
    # track position on left arr and right arr
    li = 0
    ri = 0

    while li < len(left_side) and ri < len(right_side):
        if left_side[li] <= right_side[ri]:
            new_arr.append(left_side[li])
            li += 1
        else:
            new_arr.append(right_side[ri])
            ri += 1
    
    if li < len(left_side):
        new_arr += left_side[li:]
    elif ri < len(right_side):
        new_arr += right_side[ri:]

    print("Left: ", left_side)
    print("Right: ", right_side)
    print("New: ", new_arr)
    print("")

    return new_arr



print("🦄", mergeSort(arr))