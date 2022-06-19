# Functions and Methods

# To define a function use def followed by the name of your function along with any parameters, to make a parameter
# optional add =None to the variable in the function. You may use the return keyword to RETURN the value of another
# function.. Func-Ception! Always end your function with : and indent/tab the code to execute when the function is
# called. Below is an example function named Function_Test, when called the print statement will run.

def function_test(x):
    print("This code will run when the function above Function_Test is called")


function_test(1)


# Below is a function named fun is created with two required parameters x,y and one optional parameter named z then the
# values x and y are printed and x, y are assigned values. Practice by adding the string "World" to the
# parameter z in the function then printing it to the terminal.

def fun(x, y, z=None):
    print(x, y)


fun(2.0, "Hello")


# Functions are incredibly valuable but methods are priceless! A METHOD provides reusable pieces of code for your
# program to invoke. The example below is an Instance Method - the most common method type, the first parameter will
# be the self variable in an instance method. A class name is defined, two functions are created with the (self)
# parameter along with a V variable then the method is called to and passed a value of 10.

class InstanceMethod:
    def __init__(self, V):
        self.V = V

    def s(self):
        print(self.V)


IM = InstanceMethod(10)
IM.s()

# Create a new instance method with a name of Customer with two functions named firstname and lastname then print or
# return the customer's first / last name and pass Jordan Matthews to the method.


# End of Functions and Methods
