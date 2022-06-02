import SimpleMath
import random 

def SimpleTest(test_feedback):
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    num3 = random.randrange(1, 100)
    
    student1 = SimpleMath.div(num1, num2)
    student2 = SimpleMath.div(num2, num3)
    student3 = SimpleMath.div(num1, num3)
    
    c1 = float(num1)/num2
    c2 = float(num2)/num3
    c3 = float(num1)/num3
    
    if student1 != c1 or student2 != c2 or student3 != c3:
        test_feedback.write(f"Test Failed\n Expected {c1} from {num1}/{num2} and got {student1}\nExpected {c2} from {num2}/{num3} and got {student2} \n Expected {c3} from {num1}/{num3} and got {student3}")
        return False
    return True

# running tests, not to be copied in zybooks
SimpleTest(sys.stdout)
