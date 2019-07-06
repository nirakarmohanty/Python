# Functions with Arguments

class FunctionArgument():
    print('Functions with arguments')

    def print_none(self):
        print('Print None')
    def print_two(self,*args):
        arg1,arg2=args
        print('arg1 and arg2'.format(arg1,arg2))
    def print_one(self,oneVariable):
        print(f"One Variable : {oneVariable}")

    def print_two_again(self,one,two):
        print(one, two)

object=FunctionArgument()
object.print_two("12","13")
object.print_none()
object.print_one(123)
object.print_two_again("1","2")
