from Stacks import  Stacks


def evaluate_post_fix(postfix_expression):
    expression_stack = Stacks()
    for i in range(len(postfix_expression)):
        if postfix_expression[i] != "+" and postfix_expression[i] != "*" and postfix_expression[i] != "/" \
                and postfix_expression[i] != "-":
            expression_stack.push(postfix_expression[i])
            print(postfix_expression[i])
        else:
            element_two = int(expression_stack.pop_elements())
            element_one = int(expression_stack.pop_elements())

            if postfix_expression[i] == "+":
                intermediate_result = element_one + element_two
            elif postfix_expression[i] == "*":
                intermediate_result = element_one * element_two
            elif postfix_expression[i] == "/":
                intermediate_result = int(element_one / element_two)
            else:
                intermediate_result = element_one - element_two
            expression_stack.push(intermediate_result)

    result = expression_stack.pop_elements()
    return result


if __name__ == "__main__":
    print(evaluate_post_fix(["3", "1", "+", "4", "*"]))
