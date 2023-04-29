def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func10

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    e = pow(y,1/2)*3
    r = pow(x,2/3)
    t = e + r
    return round(t,2)

b = main(8,4)
print(b)