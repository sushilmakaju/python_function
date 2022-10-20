user_input = int(input("Enter the limit : "))

def sum_of_function(limit):

    for i in range(1,limit+1):
        if i % 3 == 0 or i % 5 == 0 :
            print(i, end=" ")


sum_of_function(user_input)