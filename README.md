# CLI RPN Calculator
Code challenge for Snap Raise

Git Repo [https://github.com/jamrod/RPN_Calculator]

This program was written with python version 3.8.10 and python is the only dependency.
From the shell terminal run 'python RPN_Calc' to start the calculator.

## Requirements
Implement a command-line reverse polish notation (RPN) calculator using a language that you know well.

### Context
We're building this command-line calculator for people who are comfortable with UNIX-like CLI utilities.
We are starting with the basic 4 operators now but will want to eventually implement other operators and
an alternate interface (such as WebSocket, file, or TCP socket).
There's no need to implement these, but design with these future changes in mind.

### Specifications
1. The calculator should use standard input and standard output
2. It should implement the four standard arithmetic operators
3. The calculator should handle errors and recover gracefully
4. The calculator should exit when it receives a `q` command or an end of input 

## My Solution
I wanted to design the calculator to run in a single file with functionality split into multiple functions. My loose starting point was 
 * a function to start the calculator, instantiate top level variables and monitor whether to quit or keep running.
 *  a function to parse input
 * and a clculator function to do maths
My final RPN Calculator ended up pretty close to this initial thought, it is contained in a single file with a main function to initialize states, give the user some instructions and launch the process_input function which then receives input and reacts to it with some supporting functions. The main function creates an empty stack variable which maintains the numbers and operators that are input by the user and worked through by the other functions. The other variable instantiated in the main function is a boolean which can be set to False to exit the program.

The process_input function receives the input from the user, discards invalid characters, and builds the stack. When operand characters are received the stack is passed to the process_stack function which works through the operators and operands according to the RPN process. The calculator function is invoked to do the computations, receiving two numbers and the operator character and returning the result to process_stack which then pushes the total back on to the stack. This continues until the stack is down to one entry, which is then returned to process_input to display.

After creating the basic functionality of the calculator, I tried to anticipate failure points and design around them. Adding if else and try except blocks to manage different inputs. Through testing I realized I was not handling decimals, so I added some additional code to manage floats. I added the 'q' to quit functionality requsted in the assignment but also added a 'c' to clear out the stack in case of an error or to start a new equation. I thought about adding an 's' to show the current stack, I think it would be a useful addition but kept it simple for now.

Tests can be run by executing the test.py file. I kept the tests simple to keep free of dependencies. The test are confirming the funtionality of the supporting functions.

### Things I learned
First off I had never heard of Reverse Polish Notation before so I needed to do some research to find out what it was and how it worked; wikipedia was a good resource on the general concept and I find a blog post on i-programmer.info which explained in detail how a calculator would process the stack.
I had never tried to read an EOF on my input before so that was something I needed to look up since it was specifically requested in the spec.

### Things I might change
If I spent some more time on this I would add the ability to pass in arguments when you call the function so you could call the function with an equation and get the answer right back.