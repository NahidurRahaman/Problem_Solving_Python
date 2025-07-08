def flatten_json(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


nested = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
flat = flatten_json(nested)
print(flat)  
