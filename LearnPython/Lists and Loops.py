# Lists and Loops

# A list is a collection of data similar to an array, lists can contain any Python datatype. Below is an example
# of a list named Groceries, notice [] enclose the list and the items are comma separated.

Groceries = ["Milk", "Eggs", "Pasta Sauce"]
print(Groceries)

# You can specify a specific index you'd like to print rather than printing the whole list as such.

print(Groceries[1])

# Practice by adding Pasta to the Groceries list then print ONLY that item.

# A loop can iterate over a defined sequence - known as for each in other languages it will execute code on the first
# item and the second… etc. until the loop is broke or the loop ends. Notice a for loop starts with for i in i:
# In the example below a list is created and the loop prints each number in the list one at a time.

numbers = [1, 2, 3, 4, 6]
for num in numbers:
    print(num)

# A while loop is slightly different, it runs ONLY WHILE a specific condition is met. The example below only runs WHILE
# the value of x < 6, otherwise it will not run that code.

x = 3 + 2
while x < 6:
    print(x)
    break

# The break statement BREAKS or ends the loop, if you didn't have a break the while clause would loop forever.
# Another critical piece is the ELSE statement as shown below, this will run only if the for statement is not ran.
# Notice that the if statement only prints 3 when the number is 3, else it prints "number is not 3"

for i in numbers:
    if i == 3:
        print(i)
    else:
        print("number is not 3")

# Practice by creating a list named bucket list with the items Grand Canyon, Sequoia, and Skydiving then create a loop
# which prints all the items, one at a time. Lastly alter your loop to print Woo! when it hits Skydiving, otherwise
# print yay!


# End of List and Loops
