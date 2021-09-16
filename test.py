from RPN_Calc import *

def test_calculator():
    print("Running tests on calculator")
    assert calculator(1,2, '+') == 3, "1 + 2 is 3"
    assert calculator(4,2, '-') == 2, "4 - 2 is 2"
    assert calculator(300,300, '*') == 90000, "300 * 300 is 90000"
    assert calculator(44,4, '/') == 11, "44 / 4 is 11"
    print("All tests Passed")
    
def test_process_stack():
    print("Running tests on process_stack")
    assert process_stack([[5, 5, 5, 8], ['+', '+', '-']]) == -13, "5 5 5 8 + + - should output -13"
    assert process_stack([[5, 8], ['+']]) == 13, "5 8 + should output 13"
    assert process_stack([[5, 9, 1], ['-', '/']]) == 0.625, "5 9 1 8 - / should output 0.625"
    print("All tests Passed")

if __name__ == "__main__":
    test_calculator()
    test_process_stack()