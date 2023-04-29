def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func09

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    q = pow(y,3)
    w = pow(x,2)*y
    return (q +w)*2

b = main(2,4)
print(b)