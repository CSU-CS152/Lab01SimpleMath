# Lab01SimpleMath
Basic Input/Output Warmup Lab

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step One
1. What is the output for multiply(3, 4), and what type is it?
2. What happens if I do multiply(add(7, 2), 2)? What is the output and what type is it?
3. What is the difference between add(“3”, “4”) and add(3, 4). What do the outputs look like and why?
4. What is main doing? What is printed if the console input is 
2
9 
5. Set a variable to “dog”. What type is this?
6. Set another variable to 7 as a float using casting.

# Step Two: Coding: div(num1, num2)
Find the function div(num1, num2). As a reminder, a function is a way to break up code into repeatable bits to be reused.

Write the code for div(num1, num2) that takes in two numbers of any type and outputs a float version of num1 / num2.
For example, if someone calls the function with
div(10, 5) the function would return 2
div(5,10) the function would return 0.5

The function itself will not print or take in input from the client! (Ask yourself where that happens in the code). As such you will want to focus on the single task that is the function - and that is to simply divide two numbers.

# Step 3: Test div(num1, num2)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().

print("TESTING", div(10, 5))
print("TESTING", div(5, 10))
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Types
We are focusing on three main types in this class: int, float, and string. Ints are integers, so numbers without decimals. If you turn a decimal number into an int, it will completely cut off the decimal part, leaving only the whole number. Floats are decimal numbers, so they do not cut off the decimal, and leave it as is. Strings are essentially like sentences, words, phrases, or other info stored in "". For example, "dog", "I am", and "3 4" are all strings. 

We often want to convert our input into one of these three types because all input is read in as a string. As mentioned before, even "3 4" is a string, so it is up to us to know what **type** we are expecting, and to convert it accordingly. We see this with lines like val = int(input("what is your favorite number")). We are expecting the user to give us an int as their favorite number, so we have to convert something like "21" to 21 with int(). Similarly, casting to a float is float(), and casting to a string is str().

# Reminder on Variables
Like in math, variables are named placeholders for information. Often, in functions, you will see a lot of variable manipulation like x = y + z, where y and z are placeholders for whatever values we give them somewhere else, like in main. We **assign** values with variables with the = sign, like x = 3. In the special case of function input, like dec(3), where the dec() code is written dec(num), the computer understands an **implied** num = 3.
