def multiply(num1, num2):
    return num1 * num2
    
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def div(num1, num2):
    #student code
    return

def main():
    someNum = int(input("Give me a number: "))
    print(someNum)
    anotherNum = int(input("Give me another number: "))
    print(anotherNum)
    print(subtract(add(multiply(someNum, anotherNum), someNum), anotherNum))

if __name__ == "__main__":
    main()
