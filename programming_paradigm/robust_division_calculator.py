# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Attempt to convert numerator and denominator to float and divide.
    Returns a string with either the result or an error message.
    """
    try:
        n = float(numerator)
        d = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = n / d
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
