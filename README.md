# Lab01SimpleMath
Basic Input/Output Warmup Lab

# Below is some code. 
Please read and try to comprehend the code and then answer the questions below.

def multiply(num1, num2):
    return num1 * num2
    
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def main():
    someNum = int(input("Give me a number: "))
    print(someNum)
    anotherNum = int(input("Give me another number: "))
    print(anotherNum)
    print(subtract(add(multiply(someNum, anotherNum), someNum), anotherNum))

if __name__ == "__main__":
    main()

 What is the output for multiply(3, 4), and what type is it?

What happens if I do multiply(add(7, 2), 2)? What is the output and what type is it?

What is the difference between add(“3”, “4”) and add(3, 4). What do the outputs look like and why?

What is main doing? What is printed if the console input is 
2
9 

Set a variable to “dog”. What type is this?

Set another variable to 7 as a float using casting.
 
 Code Practice: writing div(num1, num2)
	Write the code for div(num1, num2) that takes in two numbers of any type and outputs a float version of num1 / num2.
