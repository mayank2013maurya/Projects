def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't divide a number with zero"

print(divide(1, 0))
