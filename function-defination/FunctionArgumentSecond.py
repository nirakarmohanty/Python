class FunctionArgumentSecond():
    name=''
    age=0
    experience=0
    def __init__(self):
        print(self)

    def print_fresher_5_years(self,name,age,experience):
        print("Name is {} and Age is {} and Experience is {} ".format(name,age,experience))


    def print_fresher_10_years(self,name,age,experience):
        print(f"Name is {name} and Age is {age} and Experience is {experience} ")

object = FunctionArgumentSecond()
object.print_fresher_5_years('Venkat',25,5)
object.print_fresher_10_years('Ramu',35,12)
