def calculate_factorial(value):
    if value == 1 :
        return 1

    return value * calculate_factorial(value - 1)



if __name__ == "__main__":
    print (calculate_factorial(5))
