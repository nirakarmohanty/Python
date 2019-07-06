class Calculator():

    def __init__(self):
        print("This class used to present the return type of methods")

    def addition(self,a,b):
        print(f"Addition of - First Number {a} & Second Number {b}")
        return (a+b)
    def subtraction(self,a,b):
        print(f"Subtraction of - First Number {a} & Second Number {b}")
        return (a-b)

    def multiplications(self,a,b):
        print(f"Multiplication of - First Number {a} & Second Number {b}")
        return (a*b)

    def divisions(self,a,b):
        print(f"Division of - First Number {a} & Second Number {b}")
        return (a/b)

calculator=Calculator()

addition_result=calculator.addition(1,2)
subtraction_result=calculator.subtraction(12,10)
multiplication_result=calculator.multiplications(2,5)
division_result=calculator.divisions(10,2)

print(f"ADDTION : {addition_result} " "\n"
      f"SUBTRACTION : {subtraction_result} ""\n"
      f"MULTIPLICATION : {multiplication_result}""\n"
      f"DIVISONS : {division_result}")
