# Lab01SimpleMath
Basic Input/Output Warmup Lab

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step One
Answer the following questions as comments in your code:
1. What is the output for multiply(3, 4), and what type is it?
2. What happens if I do multiply(add(7, 2), 2)? What is the output and what type is it?
3. What is the difference between add(“3”, “4”) and add(3, 4). What do the outputs look like and why?
4. What is main doing? What is printed if the console input is 
2 for the variable someNum and 
9 for the variable anotherNum?
5. Set a variable to “dog”. What type is this? (You can name the variable anything you want -- horse, var, value)
6. Set another variable to 7 as a float using casting. (You can name the variable anything you want -- num, val)

# Step Two: Coding: div(num1, num2)
Find the function div(num1, num2). As a reminder, a function is a way to break up code into repeatable bits to be reused.

Write the code for div(num1, num2) that takes in two numbers of any type and outputs a float version of num1 / num2.
For example, if someone calls the function with
```python
div(10, 5) # the function would return 2.0
div(5,10) # the function would return 0.5
```
The function itself will not print or take in input from the client! (Ask yourself where that happens in the code). As such you will want to focus on the single task that is the function - and that is to simply divide two numbers.

# Step Three: Test div(num1, num2)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().

```python
print("TESTING", div(10, 5))
print("TESTING", div(5, 10))
```
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on parameter vs input()
When writing a function, consider your parameters to be unknown information. A user may enter input with any two numbers when calling the `multiply()` function, for example multiply(3, 2) or multiply(9, 1). The numbers don't matter, and we can't assume exactly what will be entered outside of the type, either. That's the point of computer science. To write a function with a process that will work for ANY input. 

# Reminder on print() vs. return
As you have likely seen in your code, there are times when things are print()ed and times when things are returned. When we print() something, we do so to display it -- we want what we are printing to be seen. Returns, on the other hand, are useful for doing a bunch of behind the scenes work without being seen. Think of it like a game of Go Fish: when you have your pair or set of 4, you set it down for all the other players to see (or you *print()* the pair), but when you draw new cards to try to find matches, you don't want anyone to see what card you drew, you instead silently *return* it to your hand. Print displays the thing, but return actually has the physical value of the thing, so that it can be used later. Most of your functions in this class will require a return because our tests need to look at the physical value. 

A print() will always display to *something*, maybe a console, file, etc.
`print(multiply(add(7,2),2))` will display 18 to console
A return will send out the physical value
`var1 = multiply(add(7,2),2)` will catch our 18 in var1
The add(7,2) in multiply(add(7,2),2) is caught by the num1 parameter in multiply for use as a value

# Reminder on Types
We are focusing on three main types in this class: int, float, and string. Ints are integers, so numbers without decimals. If you turn a decimal number into an int, it will completely cut off the decimal part, leaving only the whole number. Floats are decimal numbers, so they do not cut off the decimal, and leave it as is. Strings are essentially like sentences, words, phrases, or other info stored in "". For example, "dog", "I am", and "3 4" are all strings. 

We often want to convert our input into one of these three types because all input is read in as a string. As mentioned before, even "3 4" is a string, so it is up to us to know what **type** we are expecting, and to convert it accordingly. We see this with lines like `val = int(input("what is your favorite number"))`. We are expecting the user to give us an int as their favorite number, so we have to convert (cast) something like "21" to 21 with int(). Similarly, casting to a float is float(), and casting to a string is str().

# Reminder on Variables
Like in math, variables are named placeholders for information. Often, in functions, you will see a lot of variable manipulation like x = y + z, where y and z are placeholders for whatever values we give them somewhere else, like in main. We **assign** values with variables with the = sign, like x = 3. In the special case of function input, like `dec(3)`, where the dec() code is written dec(num), the computer understands an **implied** num = 3.
