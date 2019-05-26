from Stacks import Stacks


def balanced_parenthesis_checker(equation):
    stacks = Stacks()
    for i in range(len(equation)):
        if (equation[i] == "("):

            stacks.push(1)

        elif (equation[i] == ")"):

            stacks.pop_elements()

    if (stacks.stack_size == 0):
        print "Equation has balanced parenthesis"

    else:
        print "Equation does not have balanced parenthesis"


balanced_parenthesis_checker("((3^2 + 8)*(5/2))/(2+6)")
