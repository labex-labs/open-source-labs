def divide():
    """A function that returns a non-zero number divided by 0

    Parameters:
    None

    Returns:
    expression: a non-zero number divided by 0.
    """
    try:
        result = 1 / 0
        return result
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
        return None

 
result = divide()
if result is not None:
    print("Result:", result)
