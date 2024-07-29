# module_MultiDictOperations.py

def merging_Dict(*args):
    """Merge multiple dictionaries into one."""
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def find_common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    common = set(args[0].keys())
    for d in args[1:]:
        common &= set(d.keys())
    return common

def invert_dict(d):
    """Invert a dictionary, grouping keys with the same value in a list."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted

def find_common_key_value_pairs(*args):
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs &= set(d.items())
    return dict(common_pairs)
