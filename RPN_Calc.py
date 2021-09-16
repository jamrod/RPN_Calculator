#RPN command line calculator

def calculator(a,b,operator):
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
            try:
                n = int(n)
            except ValueError:
                is_number = False
            if is_number:
                if contains_operator:
                    print(f"Digit out of order, {n} discarded, use 'c' to clear and restart")
                else:
                    stack[0].append(int(n))
            else:
                print(f"Invalid character {n} discarded")


    if contains_operator:
            total = process_stack(stack)
            print(total)
    else:
        print(stack[0][-1])
    
    return True

def main():
    print("""
        RPN CLI Calculator
        Only accepts these operators: +, -, * and /
        Use 'q' to quit and 'c' to clear
    """)
    active = True
    stack = [[], []]

    while active:
        active = process_input(stack)
    
    print("Exiting...")

    
        
if __name__ == "__main__":
    main()
        