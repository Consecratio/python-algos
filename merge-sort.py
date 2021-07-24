arr = [1, 4, 3, 2, 5]

def mergeSort(list):
    if len(list) == 1:
        return list

    mid = len(list) // 2

    left_side = list[:mid]
    right_side = list[mid:]

    print(left_side)
    print(right_side)

    mergeSort(left_side)
    mergeSort(right_side)

    # make a new array to merge left and right into
    new_arr = []
    # track position on left arr and right arr
    left_i = 0
    right_i = 0



mergeSort(arr)