#RPN command line calculator

def calculator(a,b,operator):
    """perform basic math operations on two digits based on operator char"""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        print("Invalid operator")
        return 0


def process_stack(s):
    """
    process the numbers and operators in RPN order, 
    arguments are passed in as a list containing 2 lists, 
    1st list is integers, second list is operators.
    calls calculator to perform maths 
    returns sum after using all operators
    """
    nums = s[0]
    ops = s[1]

    while len(ops) > 0:
        if len(nums) < 2:
            print("Error: Operators exceed Operands")
            print(f"Current State: Operands = {nums}, Operators={ops}")
            print("Suggest using 'c' to clear and start over")
            return nums[0]
        num2 = nums.pop()
        num1 = nums.pop()
        op = ops.pop(0)
        sum = calculator(num1, num2, op)
        nums.append(sum)
    return nums[-1]


def process_input(stack):
    """
    function to receive input from std.in
    handles control chars 'q' and 'c'
    discards invalid chars and builds the stack with integers and operators.
    calls process_stack when operators are received
    returns True if program should continue or False to quit
    """
    operators = ('+', '-', '*', '/')
    contains_operator = False
    try : 
        args = input('>')
    except EOFError:
        print("Received EOF")
        return False
    # print(args)
    if 'q' in args:
        return False
    if 'c' in args:
        stack[0].clear()
        stack[1].clear()
        print("0")
        return True
    if len(args) > 1:
        args = args.split()
    for n in args:
        if n in operators:
            stack[1].append(n)
            contains_operator = True
        else:
            is_number = True
            if '.' in n:
                try:
                    n = float(n)
                except ValueError:
                    is_number = False
            else:
                try:
                    n = int(n)
                except ValueError:
                    is_number = False
            if is_number:
                if contains_operator:
                    print(f"Digit out of order, {n} discarded, use 'c' to clear and restart")
                else:
                    stack[0].append(n)
            else:
                print(f"Invalid character {n} discarded")

    if contains_operator:
            total = process_stack(stack)
            print(total)
    else:
        print(stack[0][-1])
    
    return True

def main():
    """
    Initializes and runs RPN Calculator
    runs until False received from process_input
    """
    print("""
        RPN CLI Calculator
        Only accepts these operators: +, -, * and /
        Enter multiple values separated by a space 
        Use 'q' to quit and 'c' to clear
        """)
    active = True
    stack = [[], []]

    while active:
        active = process_input(stack)
    
    print("Thanks for checking this out!\nExiting...")

    
        
if __name__ == "__main__":
    main()
        