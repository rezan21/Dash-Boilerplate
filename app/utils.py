def dummy_get_y(x):
    if x == "a":
        return "b"
    if x == "b":
        return "a"
    raise ValueError("x must be a or b")  # otherwise
