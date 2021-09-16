#RPN command line calculator


def run_calc():
    print("""
        RPN CLI Calculator
    """)
    active = True
    stack = [[], []]
    total = 0

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
            print(f"Error invalid operator: {operator}")
            raise

    def process_stack(s):
        print(s)
        nums = s[0]
        ops = s[1]
    
        while len(ops) > 0:
            num2 = nums.pop()
            num1 = nums.pop()
            op = ops.pop(0)
            sum = calculator(num1, num2, op)
            nums.append(sum)
        return nums[-1]

    def process_input(stack, total):
        operators = ('+', '-', '*', '/')
        contains_operator = False
        args = input('>')
        # print(args)
        if 'q' in args:
            return False
        if len(args) > 1:
            args = args.split()
        for n in args:
            if n in operators:
                stack[1].append(n)
                contains_operator = True
            elif n.isdigit():
                stack[0].append(int(n))
            else:
                print(f"Invalid char {n} discarded")
        if contains_operator:
             total = process_stack(stack)
             print(total)
        else:
            print(stack[0][-1])
        
        return True

        

    while active:
        active = process_input(stack, total)
    
    
    print("Exiting...")

    
        
if __name__ == "__main__":
    run_calc()
        