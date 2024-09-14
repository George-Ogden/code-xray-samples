def get_nested(json_obj, key_path):
    """Get the value from a nested JSON using a key path."""
    keys = key_path.split(".")
    current_value = json_obj
    for key in keys:
        if key in current_value:
            current_value = current_value[key]
        else:
            raise KeyError(f"Key '{key}' not found.")
    return current_value


def set_nested(json_obj, key_path, value):
    """Set the value in a nested JSON using a key path."""
    keys = key_path.split(".")
    current_value = json_obj
    for key in keys[:-1]:
        if key not in current_value:
            current_value[key] = {}
        current_value = current_value[key]
    current_value[keys[-1]] = value


def update_field_name(json_obj, old_key_path, new_key):
    """Rename a field in a nested JSON."""
    keys = old_key_path.split(".")
    current_value = json_obj
    for key in keys[:-1]:
        current_value = current_value.get(key, {})

    if keys[-1] in current_value:
        current_value[new_key] = current_value[keys[-1]]
    else:
        raise KeyError(f"Key '{keys[-1]}' not found in {old_key_path}")
