"""
    [6, 9, 2, 7, 3, 4, 0]
        min 3  =>  [3, 4, 6, 7, 9]
        max 3  => [0, 2, 3]
        min, max 3  => [3]
"""

def limit(arr, min=None, max=None):
    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)

    return [val for val in sorted(arr) if min_check(val) and max_check(val)]


print(limit([6, 9, 2, 7, 3, 4, 0], 4, 8))