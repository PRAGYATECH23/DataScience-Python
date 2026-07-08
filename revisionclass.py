# x=5
# print(x,type(x))
# x="Hello World!"
# print(x,type(x))
# x=20
# print(x,type(x))
# x=20.5
# print(x,type(x))
# x=1j
# print(x,type(x))
# x=["apple","banana","cherry"]
# print(x,type(x))
# x=("apple","banana","cherry")
# print(x,type(x))
# x=range(6)
# print(x,type(x))
# x={"name" : "John", "age" : 36}
# print(x,type(x))
# x={"apple", "banana", "cherry"}
# print(x,type(x))
# x=frozenset({"apple", "banana", "cherry"})
# print(x,type(x))
# x=True
# print(x,type(x))
# x=b"Hello"
# print(x,type(x))
# x=bytearray(5)
# print(x,type(x))
# x=memoryview(bytes(5))
# print(x,type(x))
# x=None 
# print(x,type(x))

# student_name="Khushi"
# age=19
# marks=4
# print(f'Student: {student_name},Age: {age},Marks:{marks}')

# x=y=z=0
# a,b,c=10,20,30
# print(x,y,z)
# print(a,b,c)

'''Operators
1.Arithmetic
2.Assignment
3.Comparison
4.Logical
5.Membership
6.Bitwise
7.Identity'''

# print(10//4)
# print(9%4)
# print(2**6)

# monthly_salary=float(input('Monthly salary (Rs.):'))
# annual_salary=monthly_salary*12
# daily_salary=monthly_salary/30
# tax=annual_salary*0.10 #10% tax
# print(f'Annual: Rs.{annual_salary:,.0f}')
# print(f'Daily: Rs.{daily_salary:,.2f}')
# print(f'Tax: Rs.{tax:,.2f}')
# print(f'Net: Rs.{annual_salary-tax:,.0f}')

#Assignment Operators

#Shift keys
# print(2>>1)
# c=2
# c<<=2  c=c<<2
# print(c>>1)

#Logical Operators
'''and =>& =>multiplication 
or=>|=> addition'''
# a=20
# b=30
# print(a<b and a==20)
# print(a>b | a==20)
# print(a>b or b==20)
# print(a<b & b==20)

#Identity Operators
# print(a is b)
# print(a is not b)

# x=["Maruti","BMW"]
# y=["Maruti","BMW"]
# z=x
# print(x is y)
# print(x is z)
# print(y is z)
# print(x is not y)
# print(x is not z)
# print(y is not z)

# x=10
# y=10
# z=x
# u=y
# print(x is z)
# print(z is x)
# print(y is u)
# print(u is y)
# print(x is not y)
# print(x is not z)
# print(y is not z)

#Membership Operators

# x=["Maruti","BMW"]
# print("Maruti"in x)
# print("Maruti1"in x)
# print(" Maruti"in x)
# print("maruti" not in x)

# 1024 bytes=1 kbytes

'''
0 1 2 3 4 5 6 7 8 9 =>10
0 1 =>2
0 1 2 3 4 5 6 7 10 11 12 13 14 15 16 17 20 .....=>8
0 1 2 3 4 5 6 7 8 9 A B C D E F 10....=> 16'''

# print(10+10.0)

# #Input Function

# number1=input("Enter a number:")
# print(number1)
# print(type(number1))
# # print(number1+10)


# number1=int(input("Enter a number:"))
# print(number1)
# print(type(number1))
# print(number1+10)

# print("Hello"+",how are you?")

# x= int(input("Enter first value for sum:"))
# y= int(input("Enter second value for sum:"))
# z=x+y
# print("Sum:",z)

# name=input("Enter your name:")
# age=input("Enter your age:")
# gpa=float(input("Enter your gpa:"))
# print(name)
# print(type(name))
# print(age)
# print(type(age))
# print(gpa)
# print(type(gpa))

# #Calculating hypotenuse 
# p=int(input("Enter the length of perpendicular:"))
# b=int(input("Enter the length of base:"))
# h=((p**2)+(b**2))**(1/2)
# print("Hypotenuse=",h)

# print(123,end="---")
# print(456,end="---")
# print(789)
# #printing a pattern
# print("+"+"-"*10+"+")
# print(("|"+" "*10+"|\n")*5,end="")
# print("+"+"-"*10+"+")

#string manipulation
#accessing characters from string
city="Bhopal"
# print(city[0])
# print(city[2])
# print(city[-1])
# print(city[-3])
# print(city[1])
# print(city[3])
# print(city[4])
# print(city[5])
# print(city[-2])
# print(city[-4])
# print(city[-5])
# print(city[-6])

#Slicing string[start:stop:step]
# name="Pragya Sisodiya"
# print(name[0:6])
# print(name[6:])
# print(name[:6])
# print(name[::2])
# print(name[::-1])

#Length of the string
# print(len(city))
# print(len(name))

#text=" Hello python World ! "

# #Case
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# #Strip Whitespace
# print(text.strip())

# #Search
# print('python' in text)
#print(text.find('python1'))
# print(text.count('l'))

# str="hello how are YOU?"
# print(str.capitalize())

#06/07/2026   Monday

# text=" Hello python World ! "
# #Replace
# print(text.replace('Python','AI'))

# #Split and Join
# csv='Rahul,22,Bhopal,Engineer'
# parts=csv.split(',')
# print("Parts:",parts)
# print(parts[0])
# rejoined='|'.join(parts)
# print("rejoined:",rejoined)

# #Check content
# print('hello123'.isalnum())
# print('hello123*'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print(' '.isspace())

# #Start/end check
# email='student@gmail.com'
# #a@b.c
# print(email.endswith('.com'))
# print(email.startswith('stu'))

#Multiple assignment in strings
# name,cgpa,rank='Pragya',9.2875,6
# print(name,cgpa,rank)

# #Basic
# print(f'Hello,{name}!')

# #Format numbers
# print(f'cgpa: {cgpa:.2f}')
# print(f'cgpa: {cgpa:.0f}')  #rounded
# print(f'Count: {1000000:,}')

# #Padding and alignment
# print(f'{name:<15}|{cgpa:>8.2f}|Cgpa:{cgpa}')

# name="Pragya Sisodiya"
# print(f'{name:<15}|{cgpa:>8.2f}|Cgpa:{cgpa}')

# #Expressions inside {}
# price,gst=500,0.18
# print(f'Price:Rs.{price}|GST:Rs.{price*gst:.2f}|Total:Rs.{price*(1+gst):.2f}')

# If else statement

#Read two numbers
# number1=int(input("Enter  the first number:"))
# number2=int(input("Enter the second number:"))

# #Choose the larger
# if number1>number2:
#     larger_number=number1
# else:
#     larger_number=number2

# #Print the result
# print("The larger number is:",larger_number)

#Largest of three numbers

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# num3=int(input("Enter the third number:"))

# largest_number=num3

# if num1>largest_number:
#     largest_number=num1
# if num2>largest_number:
#     largest_number=num2

# print("The largest number is ",largest_number)

# largest_number=max(num1,num2,num3)
# lowest_number=min(num1,num2,num3)

# print("The largest number is:",largest_number)
# print("The lowest number is :",lowest_number)

#WHILE LOOP
# while True:
#     print("i 'm  stuck inside a loop.")

#Printing largest number
# largest_number=-9999999

# number=int(input("Enter a number:"))

# while number!=-1:
#     if number> largest_number:
#         largest_number=number
#     number=int(input("Enter a number:"))
# print("The largest number is:",largest_number)

# lowest_number=9999999

# number=int(input("Enter a number or type -1 to stop:"))

# while number!=-1:
#     if number< lowest_number:
#         lowest_number=number
#     number=int(input("Enter a number or type -1 to stop:"))
# print("The lowest number is:",lowest_number)

# counter=0
# while counter <100:
#     print(counter)
#     counter+=1
# print("*************************")

# #For loop
# for count in range(100):
#     print(count)

'''
condition based while loop
iteration based for loop
'''

# exit=0
# while exit!=1:
#     exit=int(input("Enter a number:"))
#     print(exit)

# for i in range(10):
#     print("The value of counter is currently:",i)

# for i in range(2,8):
#     print("The value of counter is currently:",i)

# for i in range(2,8,3):    #range(start,stop,step)
#      print("The value of counter is currently:",i)

# for i in range(1,1):    #it will print nothing
#      print("The value of counter is currently:",i)

# for i in range(2,1):    #range(start,stop,step)
#     print("The value of counter is currently:",i)

# power=1
# for expo in range (16):
#     print("2 to the power of ",expo,"is",power)
#     power*=2


#Break 

# power=1
# for expo in range (16):
#     print("2 to the power of ",expo,"is",power)
#     power*=2
#     if expo==7:
#         break
# print("************mow I am out***********")

# #Continue  (next iteration pr chlo)

# power=1
# for expo in range (16):
#     if expo==7:
#         continue
#     print("2 to the power of ",expo,"is",power)
#     power*=2
# print("************mow I am out***********")

# print("The break instrucions:")
# for counter in range(1,6):
#     if counter ==4:
#         break
#     print("Inside the loop",counter)
# print("Outside the loop.")

# print("\nThe continue instrucions:")
# for counter in range(1,6):
#     if counter ==4:
#         continue
#     print("Inside the loop",counter)
# print("Outside the loop.")


# largest_number=-99999999
# counter=0
# while True:
#     number=int(input("Enter a number or type -1 to end the program:"))
#     if number==-1:
#         break
#     counter+=1
#     if number>largest_number:
#         largest_number=number
#     print(counter)
# if counter!=0:
#     print("The largest number is :",largest_number)
# else:
#     print("You haven't entered a number.")

















    





