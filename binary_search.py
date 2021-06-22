"""
    binary search
        [2, 3, 4, 6, 12, 19, 20, 21], 12  =>  4
"""

def binary_search(array, element):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (high + low) // 2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return None


print(binary_search([2, 3, 4, 6, 12, 19, 20, 21], 19))