def reverse_a_string(original_string):
    reverse_string = None
    if len(original_string) < 2:
        return original_string[0]

    part_1_input = original_string[0:int(len(original_string)/2)]
    part_2_input = original_string[int(len(original_string)/2):]

    return reverse_a_string(part_2_input) + reverse_a_string(part_1_input)



if __name__ == "__main__":
    print(reverse_a_string("Shivam"))
    print(reverse_a_string("Ashi"))