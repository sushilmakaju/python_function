user_input = None
user_num = 0
user_num2 = 0
sum = 0

def output_bill():
    print("------- Main Menu -------")
    print("1. Add")
    print("0. Exit")
    print("-------------------------")

def input_function():
    global user_input
    user_input = int(input("Enter your choice (0->exit) : _"))

def sum_function():
    global user_num
    global user_num2
    global sum

    user_num = int(input("Enter first no : _"))
    user_num2 = int(input("Enter second no : _"))
    sum = user_num + user_num2
    print("Sum: {}".format(sum))

output_bill()
input_function()

while user_input == 1 :
    sum_function()
    output_bill()
    input_function()

print("Bye!")

