# module_SetOperations.py

def add_element(s, elem):
    """Add an element to the set."""
    s.add(elem)
    return s

def remove_element(s, elem):
    """Remove an element from the set, if present."""
    s.discard(elem)
    return s

def union_intersection(s1, s2):
    """Return the union and intersection of two sets."""
    return s1 | s2, s1 & s2

def difference(s1, s2):
    """Return the difference S1 - S2."""
    return s1 - s2

def is_subset(s1, s2):
    """Check if S1 is a subset of S2."""
    return s1 <= s2

def set_length(s):
    """Return the length of the set without using len()."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Return the symmetric difference of two sets."""
    return s1 ^ s2

def power_set(s):
    """Return the power set of a given set."""
    from itertools import chain, combinations
    s = list(s)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def unique_subsets(s):
    """Return all unique subsets of a given set."""
    s = list(s)
    subsets = set()
    for i in range(1 << len(s)):
        subset = frozenset(s[j] for j in range(len(s)) if i & (1 << j))
        subsets.add(subset)
    return subsets
