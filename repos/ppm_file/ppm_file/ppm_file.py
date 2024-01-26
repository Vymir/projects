def calc_parser(calc_str):

    # If the expression is just a number, return it as an integer.
    if calc_str.isdigit():
        return int(calc_str)

    # Find the operator and the operands.
    operator_index = calc_str.find(" ")
    operator = calc_str[operator_index]
    operand1 = calc_str[:operator_index].strip()
    operand2 = calc_str[operator_index + 1:].strip()

    # Recursively calculate the values of the operands.
    operand1_value = calc_parser(operand1)
    operand2_value = calc_parser(operand2)

    # Perform the operation and return the result.
    if operator == "+":
        return operand1_value + operand2_value
    elif operator == "-":
        return operand1_value - operand2_value


print(calc_parser("11 + (4 + 5) - (5+ 4 - 3)"))