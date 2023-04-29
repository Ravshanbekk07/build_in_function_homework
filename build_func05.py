def main(n, x):
    """Integer type variables 'n' and 'x' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func05

    Args:
        n (int): integer
        x (int): integer
        
    Returns:
        int: the value of the expression
    """
    v = pow(6,3)
    n = pow(3,6)
    m = n+v
    return m

b = main(3,6)
print(b)