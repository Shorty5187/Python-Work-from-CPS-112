# Selection Sort
#   - At pass i, find smallest remaining value in range [i, n-1]
#   - and place it at position i
def sort_selection( data ):
    n = len(data)

    for i in range(0, n-1):#last value looked at is n-2
        small_at = i

        for j in range(i+1, n):
            if data[j] < data[small_at]:
                small_at = j

        if i != small_at:
            data[i], data[small_at] = data[small_at], data[i]


# Insertion Sort
#   - At pass i, shift all larger values before it, in the range [0, i-1], down
#   - freeing up position for it
def sort_insertion( data ):
    n = len(data)

    for i in range(1, n):  # 1 to n-1
        hold = data[i]

        j = i-1
        while j >= 0 and data[j] > hold:
            data[j+1] = data[j]
            j -= 1

        # avoid moving it back if it was the largest
        if j+1 != i:
            data[j+1] = hold


# Insertion Sort
#   - At pass i, shift all larger values before it [0, i-1] down
#   - freeing up position for it
def sort_insertion_segment( data, left, right ):
    for i in range(left+1, right+1):
        hold = data[i];

        j = i-1
        while j >= left and data[j] > hold:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = hold


# ------------------------------------------------------
# Recursively sort the partition [left, right]
def sort_quick_nr(data):
    sort_quick(data, 0, len(data)-1)

#def sort_quick(data, left=None, right=None):
def sort_quick(data, left, right):
#    if left is None or right is None:
#        left = 0
#        right = len(data)-1

    # Select and place the pivot value in the leftmost position
    place_pivot(data, left, right)

    # Partion the list placing the pivot value between the two partitions
    divPos = partition(data, left, right)

    # Sort the left partition
    if left < divPos - 1:
        sort_quick(data, left, divPos - 1)

    # Sort the right partition
    if divPos + 1 < right:
        sort_quick(data, divPos + 1, right)

# Select and place pivot
#   - select the middle value as dividing value
def place_pivot(data, left, right):
    mid = (left + right) // 2

    data[left], data[mid] = data[mid], data[left]

# Partition
def partition(data, left, right):
    pivot_value = data[left]

    look_right = left + 1    # Starts at the left and works right looking for the next value belonging in the right partition
    look_left = right        # Starts at the right and works left looking for the next value belonging in the left partition

    while look_right <= look_left:
        while (look_right <= look_left) and (data[look_right] <= pivot_value):
            look_right += 1

        while (look_left >= look_right) and (data[look_left] >= pivot_value):
            look_left -= 1

        # Now swap the two values belonging in the opposite partitions
        if look_right < look_left:
            data[look_left], data[look_right] = data[look_right], data[look_left]

            look_right += 1
            look_left  -= 1

    # place the pivot value between two partitions
    data[left] = data[look_left]
    data[look_left] = pivot_value

    return look_left


