def flatten_nested_dict(nested_dict):
    """Flattens a nested dictionary into a single level dictionary."""
    flat_dict = {}
    def flatten(current_dict, parent_key=''):
        for key, value in current_dict.items():
            new_key = f'{parent_key}.{key}' if parent_key else key
            if isinstance(value, dict):
                flatten(value, new_key)
            else:
                flat_dict[new_key] = value
    flatten(nested_dict)
    return flat_dict