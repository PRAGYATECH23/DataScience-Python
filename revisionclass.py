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

# i=1
# j=not not i
# print(i)
# print(j)

# numbers=[10,5,7,2,1]
# print(numbers)
# print(type(numbers))

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])

# numbers[3]=20
# print(numbers)

# numbers[2]=numbers[0]
# print(numbers)
# numbers[2],numbers[1]=numbers[1],numbers[2]
# print(numbers)

# del numbers[4]
# print(numbers)

# print(len(numbers))
# lengthOfList=len(numbers)
# print(numbers)

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])

# a=10
# # print("Variable a:",a)
# print("Address of Variable a in integer:",id(a))
# print("Address of Variable a in hexadecimal:",hex(id(a)))

# print(hex(id(numbers)))
# print(hex(id(numbers[0])))
# print(hex(id(numbers[1])))
# print(hex(id(numbers[2])))
# print(hex(id(numbers[3])))

# hat=[1,2,3,4,5]
# print(len(hat))

# del hat[len(hat)-1]
# print(hat)

#10/7/2026  Friday
# #append & insert function
#list.append(value)
#list.insert(location,value)

# list=[5,4,3,2,1]
# print(len(list))
# print(list)

# list.append(6)
# print(len(list))
# print(list)

# list.insert(0,222)
# print(len(list))
# print(list)

#Traversing a list

# list1=[1,2,3,4,5,6,7,8,9,10]
# for index in range(len(list1)):  #i=iterator=index
#     print(index)
#     print(list1[index])

# index=0
# while index<len(list1):
#     print(list1[index])
#     index+=1

#Updating a list in loop
# list=[]
# for i in range(1,11):
#     list.append(i)
# print("list:",list)

# list=[]
# iterator=1
# while iterator<11:
#     list.append(iterator)
#     iterator+=1
# print(list)

# list=[]
# for i in range(21,31):
#     # list.insert(i,i)
#     list.append(i)
# print("list:",list)

# my_list=[10,20,30,40,50,60,70,80,90,100]
# for index in range(len(my_list)):
#     my_list[index] += 1
# print(my_list)
# sum=0
# for i in range(len(my_list)):
#     sum+=my_list[i]
# print("Sum:",sum)

# for element in my_list:
#     sum+=element
# print("sum:",sum)

# index=0
# for element in my_list:
#     print("my_list[",index,"]=>",element)
#     index+=1

#Copying a variable into another variable
# a=10
# b=20

# print("a:",a)
# print("b:",b)

# print("-------------")

# temp=b
# b=a
# a=temp
# print("a:",a)
# print("b:",b)

#copying/swapping
# a,b=b,a
# print("a:",a)
# print("b:",b)

# my_list=[10,20,30,40,50,60,70,80,90,100]
# print(my_list)
# #swap-2nd and 5th values

# my_list[1],my_list[4]=my_list[4],my_list[1]
# print(my_list)

# lst=[]
# del lst
# print(lst)

#14/07/26    Tuesday
#bubble sort

# list=[8,10,6,2,4]
# print(list)
# count=0
# for index in range(len(list)-1):
#     #for index_inner in range(len(list)-1):
#     for index_inner in range(len(list)-1-index):
#         count+=1
#         if list[index_inner]>list[index_inner+1]:
#             list[index_inner],list[index_inner+1]=list[index_inner+1],list[index_inner]

# print("Sorted List:",list)
# print("my loop is running for",count,"times")

'''
Dry Run
Current list     [8,10,6,2,4]

index(0-3)          0         1          2          3
index_inner(0-3)    0 1 2 3   0 1 2 3    0 1 2 3    0 1 2 3 

index      index_inner      sorted_list
0          0                [8,10,6,2,4]  
           1                [8,6,10,2,4] 
           2                [8,6,2,10,4]
           3                [8,6,2,4,10]
           
1          0                [6,8,2,4,10]
           1                [6,2,8,4,10]
           2                [6,2,4,8,10]
           3                [6,2,4,8,10]
           
2          0                [2,6,4,8,10]
           1                [2,4,6,8,10]'''

'''best case- sorted list
worst case -descending order of list
'''
# list=[1,2,3,4,5]
# print(list)
# count=0
# swapped=False
# for index in range(len(list)-1):
#     #for index_inner in range(len(list)-1):
#     for index_inner in range(len(list)-1-index):
#         count+=1
#         if list[index_inner]>list[index_inner+1]:
#             list[index_inner],list[index_inner+1]=list[index_inner+1],list[index_inner]
#             swapped=True
#     if not swapped:
#         break

# print("Sorted List:",list)
# print("my loop is running for",count,"times")

#
# list=[8,10,6,2,4]
# #list.sort()
# list=sorted(list)
# print(list)

# list.reverse()
# print(list)

# lst=['D','F','A','Z']
# lst.sort()
# print(lst)

# a=3
# b=1
# c=2
# lst=[a,c,b]
# lst.sort()
# print(lst)

# print(ord("A"))

# list_1=[1]
# list_2=list_1[:]
# list_1[0]=2
# print(list_2)

# my_list=[10,8,6,4,2]
# new_list=my_list[0:3]
# print(new_list)


# my_list=[10,8,6,4,2]
# new_list=my_list[1:-1]
# print(new_list)


# my_list=[10,8,6,4,2]
# new_list=my_list[-1:1]
# print(new_list)


# my_list=[10,8,6,4,2]
# new_list=my_list[:3]
# print(new_list)


# my_list=[10,8,6,4,2]
# del my_list[1:3]
# print(new_list)


# my_list=[10,8,6,4,2]
# del my_list[:]
# print(my_list)


# my_list=[10,8,6,4,2]
# del my_list
# print(my_list)

# my_list=[0,3,12,8,2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# lst = [ 3, 11, 5, 1,17, 9, 7, 15, 13]
# largest_num=lst[0]
# for i in range(1,len(lst)):
#     if lst[i]>largest_num:
#         largest_num=lst[i]
# print("The largest no. is",largest_num)

list_1=["A","B","C"]
list_2=list_1
list_3=list_2
del list_1[0]
del list_2[0]
print(list_3)

list_1=["A","B","C"]
list_2=list_1
list_3=list_2
del list_1[0]
del list_2
print(list_3)

list_1=["A","B","C"]
list_2=list_1
list_3=list_2
del list_1[0]
del list_2[:]
print(list_3)


list_1=["A","B","C"]
list_2=list_1[:]
list_3=list_2[:]
del list_1[0]
del list_2[0]
print(list_1)
print(list_2)
print(list_3)


































    





