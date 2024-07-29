# module_ListFunction.py

def find_max(lst):
    """Return the maximum value in the list."""
    if not lst:
        return None
    return max(lst)

def find_min(lst):
    """Return the minimum value in the list."""
    if not lst:
        return None
    return min(lst)

def calculate_sum(lst):
    """Return the sum of all elements in the list."""
    return sum(lst)

def calculate_average(lst):
    """Return the average of the list."""
    if not lst:
        return None
    return sum(lst) / len(lst)

def find_median(lst):
    """Return the median of the list."""
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
