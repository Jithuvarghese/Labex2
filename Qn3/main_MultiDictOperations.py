import module_MultiDictOperations as mdo

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}
dict3 = {'c': 3, 'd': 5, 'e': 6}

# Merging dictionaries
merged_dict = mdo.merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged_dict)

# Finding common keys
common_keys_result = mdo.find_common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)

# Inverting a dictionary
inverted_dict = mdo.invert_dict(dict1)
print("Inverted Dictionary:", inverted_dict)

# Finding common key-value pairs
common_pairs = mdo.find_common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)
