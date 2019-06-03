
def print_sum_of_integers(value):
    if value == 1:
        return 1


    return value + print_sum_of_integers(valu e -1)


if __name__ == "__main__":
    print(print_sum_of_integers(3))
