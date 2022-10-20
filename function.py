# def add (num1, num2):
# 	total = num1 + num2
# 	return total
#
# total = add(2,5)
# print(total)

# Variable Scope
#local Scope
# num1 = int(input("N1>> :"))
# num2 = int(input("N2>> :"))
# def add():
#     b = 5
#     c=10
#     d = b + c
#     print(d)
# add()

# num1 = int(input("N1>> :"))
# num2 = int(input("N2>> :"))
# def add ():
#     # to call global variable in local variable
# 	global num1
# 	global num2
# 	return num1 + num2
#
# total = add()
# print(total)
# print(num1, num2)

# non local


# def f1 ():
# 	sum = 40
# 	def f2():
# 		nonlocal sum
# 		print(sum)
# 	f2()
#
# f1()


# Arguments
#1 General Arguments/Positional/Required


# def add (a,b,c,d=5):
# 	return a+b+c+d
#
# sum = add(2,5,d=10,c=6)
# print(sum)



# global varible
#
# a = int(input("n1>>> : "))
# b = int(input("n2>>> : "))
# def add(c,d):
#     total = c + d
#     return total
# total = add(a,b)
# print(total)




#
# #function
# def add(a,b):
#     return a+b
# def print_value(result):
#     print("Result = ",result)
# total =  add(20, 30)
# print_value(total)

# scope of variable
#Global variable
# def add (num1, num2):
# 	total = num1 + num2
# 	return total
#
# total = add(2,5)
# print(total)

# a = 50
# def function_1(num1):
#     print(num1)
# function_1(a)
# def function_2(num1):
#     result = num1+ a
#     return result
# function_2(30)


#function classwork
#1
# a = int(input("N1>>> : "))
# b = int(input("N2>>> : "))
# def max_num(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# result = max_num(a,b)
# print("the maximum number is ",result)

#2
# num1 = int(input("enter a number"))
# def fiz_buzz(num1):
#     if (num1%3 == 0 and num1%5 == 0):
#         print("Fizzbuzz")
#     elif (num1 % 3 == 0):
#         print("Fizz")
#     elif (num1 % 5 == 0):
#         print("Buzz")
#     else:
#      print(num1)
# fiz_buzz(num1)

#3
# sped= int(input("enter speed : "))
# def speed_check(speed):
#     demerits = 0
#     overspeed = 0
#     if speed <= 70:
#         print("ok")
#     elif speed > 70:
#         overspeed = speed - 70
#         demerits = overspeed // 5
#         if demerits > 12:
#             print("license suspended", demerits)
#         else :
#             print(demerits)
#
# speed_check(sped)

#4
# number = int(input("enter a number"))
# def show_number(limit):
#     for i in range(0,limit+1):
#         if i%2 == 0:
#             print(i, "even")
#         else:
#             print(i, "odd")
# show_number(number)


# num1 = int(input("enter a number"))
# num2 = int(input("enter second number"))
# sum = num1 + num2
# print(sum)


#Write a function called show_stars(rows). If rows is 5, it should print the following:

# a=0
# def show_stars(a):
#  for i in range(1,5):
#     for j in range(1, i+1):
#         print("*", end= " ")
#     print()
# show_stars(a)
















