# main_SetOperations.py

import module_SetOperations as mso

# Create some example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
empty_set = set()

# Demonstrate add_element
print("Original set:", set1)
set1 = mso.add_element(set1, 6)
print("After adding 6:", set1)

# Demonstrate remove_element
print("\nOriginal set:", set1)
set1 = mso.remove_element(set1, 3)
print("After removing 3:", set1)

# Demonstrate union and intersection
union_set, intersection_set = mso.union_intersection(set1, set2)
print("\nUnion of set1 and set2:", union_set)
print("Intersection of set1 and set2:", intersection_set)

# Demonstrate difference
difference_set = mso.difference(set1, set2)
print("\nDifference (set1 - set2):", difference_set)

# Demonstrate is_subset
is_subset_result = mso.is_subset(set1, set2)
print("\nIs set1 a subset of set2?:", is_subset_result)

# Demonstrate set_length
length_of_set1 = mso.set_length(set1)
print("\nLength of set1:", length_of_set1)

# Demonstrate symmetric_difference
sym_diff_set = mso.symmetric_difference(set1, set2)
print("\nSymmetric difference of set1 and set2:", sym_diff_set)

# Demonstrate power_set
power_set_of_set1 = mso.power_set(set1)
print("\nPower set of set1:")
for subset in power_set_of_set1:
    print(subset)

# Demonstrate unique_subsets
unique_subsets_of_set1 = mso.unique_subsets(set1)
print("\nUnique subsets of set1:")
for subset in unique_subsets_of_set1:
    print(subset)
