#print("Hello, World!")

#print("Hello")
#print("How")
#print("Are")
#print("you")
#print("Pragya")

#identifying the datatype
# age=4
# print(age)
# print(type(age))

# age="Four"
# print(age)
# print(type(age))

# name="Pragya"
# age=19
# print("My name is",name,".","I am ",age,"years old.")

#Datatypes
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
# x=None print(x,type(x))

#Operators

#arithmetic operators
# print("10+2=",10+2) 
# print("10-2=",10-2)
# print("10*2=",10*2)
# print("10/2=",10/2)
# print("10//2=",10//2)
# print("10%2=",10%2)
# print("9%5=",9%5)
# print("10//3=",10//3)
# print("2**3=",2**3)
# print("5%3=",5%3)
# print("5%-3=",5%-3)

'''
    x    y     x&y
    0    0     0
    1    0     0
    0    1     0
    1    1     1

    x    y     x|y
    0    0     0
    1    0     1
    0    1     1
    1    1     1
    '''
# print(5&3)
# print(5|3)

#assignment operators

# x=5
# print(x)
# x+=3
# print(x)
# x-=2
# print(x)
# x*=3
# print(x)
# x/=2
# print(x)
# x//=3
# print(x)
# x**=2
# print(x)
# x=5
# x%=3
# print(x)
# x&=3
# print(x)
# x|=2
# print(x)
# x^=3
# print(x)


#comparison operators
# a=10
# b=20
# print("a==b:",a==b)
# print("a==10:",a==10)
# print("a!=b:",a!=b)
# print("a!=10:",a!=10)
# print("a>b:",a>b)
# print("a<b:",a<b)
# print("a>=b:",a>=b)
# print("a<=b:",a<=b)
# print("a>=10:",a>=10)
# print("a<=10:",a<=10)

#logical operators
# x=6
# print(x<5 and x<10)
# print(x<5 or x<4)
# print(not(x<5 and x<10))

#identity operators
# x=3
# y=3

# print(x is y)
# print(x is not y)
# y=4
# print(x is y)
# print(x is not y)

# x=["Maruti","BMW"]
# y=["Maruti","BMW"]
# z=x
# print("x is y:",x is y)
# print("y is z:",y is z)
# print("x is z:",x is z)

# print("x is not y:",x is not y)
# print("y is not z:",y is not z)
# print("x is not z:",x is not z)

# x=10
# y=10
# print(x is y)

# x=["Maruti","BMW"]
# y=["Maruti","BMW"]
# print(x is y)

#Membership operators
# print("Maruti" in x)
# print("Maruti" not in x)

# print("Maruti1" in x)
# print("Maruti1" not in x)

#Bitwise operators
# x=10  #0000 1010
# y=20  #0001 0100
# print(x&y)
# print(x|y)
# print(x^y)
# print(~x)
# print(~y)
# print(x<<2)
# print(y<<2)
# print(x>>2)
# print(y>>2)

#input function
# name=input("Please enter your name:")
# print("Hello",name)
# age=input("Please enter your age:")
# print("Hello",name, "You are",age, "Years Old")
# phone=input("Please enter your phone no.:")
# print("Contact no.",phone)
# email=input("Please enter your email:")
# print("email:",email)

#ADDING TWO OPERANDS BY THE ARITHMETIC OPERATOR "+"
#type casting
# x= int(input("Enter first value for sum:"))
# y= int(input("Enter second value for sum:"))
# z=x+y
# print("Sum:",z)

# x= input("Enter first value for sum:")
# y= input("Enter second value for sum:")
# z=int(x)+int(y)  #type casting
# print("Sum:",z)

#string concatenation
# x= input("Enter first value for sum:")
# y= input("Enter second value for sum:")
# z=x+y
# print("Sum:",z)

# x= input("Enter first value for sum:")
# y= input("Enter second value for sum:")
# z=int(x+y)
# print("Sum:",z)

#print(1+"2")
#print("1"+2)  #unsupported operand type

#calculating hypotenuse
# p=int(input("Enter the perpendicular:"))
# b=int(input("Enter the base:"))
# h=((p**2)+(b**2))**(1/2)  #IMPORTANCE OF BRACKETS
# print("Hypotenuse:",h)

# p=6
# b=8
# h=((p**2)+(b**2))**(1/2)
# print("Hypotenuse:",h)

#09/06/2026  Tuesday

#pattern printing
#static logic
# print("+-----------+")
# print("|           |")
# print("|           |")
# print("|           |")
# print("|           |")
# print("|           |")
# print("+-----------+")

# # # #dynamic logic
# # print("+"+"-"*10+"+")
# # print(("|"+" "*10+"|\n")*5 , end="")
# # print("+"+"-"*10+"+")

# #property of print "end"
# print("Hello How are you?",end="\n")
# print("I am good")

#string manipulation
#accessing characters from string
# city="Bhopal"
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


# Decision making in python
# print(2==2)
# print(2==2.)

# var=0 #Assigning 0 to var
# print(var==0)

# var=1 #Assigning 1 to var
# print(var==0)

# print(("+"+"-"*10+"+"+"\n")+(("|"+" "*10+"|\n")*5)+("+"+"-"*10+"+") )
#conditional execution
#if 
# var=11
# if var==11:
#     print("Var is 11")
# print("Hello")

#10/06/2026 Wednesday

# number1 = int(input("Enter the first number:"))
# number2 = int(input("Enter the second number:"))
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# print("Larger number:",larger_number)

# if number1 > number2: larger_number = number1
# else: larger_number = number2
# print("Larger number:",larger_number)

# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))

# largest_number=a

# if b>largest_number:
#     largest_number=b
# if c>largest_number:
#     largest_number=c
# print("the largest number  is:",largest_number)

#printing minimum & maximum no.

# largest_number=max(a,b,c)
# lowest_number=min(a,b,c)

# print("The largest number is:",largest_number)
# print("The lowest number is :",lowest_number)

#While_loop
# while True:
#     print("I 'm stuck inside a loop.")

#Printing largest number
# largest_number=-99999999

# number =  int(input("Enter a number or type -1 to stop:"))

# while number !=-1:
#     if number> largest_number:
#        largest_number=number
#     number=int(input("Enter a number or type -1 to stop:"))
# print("The largest number  is:",largest_number)

#11/06/2026  Thursday

# number=int(input('Enter a number:'))
# even=0
# odd=0
# while number !=0:
#     if number%2==0:
#         even+=1
#     else:
#         odd+=1
#     number=int(input('Enter a number:'))
# print("Even:",even)
# print("Odd:",odd)

# print(bool(1))
# print(bool(-1))
# print(bool(0))

# print(bool())
# print(bool(None))


# print(bool("a"))
# print("b")
# print(" ")
# print("")


#counter variable
# counter=5
# while counter!=0:
#     print("Inside the loop.",counter)
#     counter-=1
# print("Outside the loop.",counter)

#Truthy /Falsy value
# counter=5
# while counter:
#     print("Inside the loop.",counter)
#     counter-=1
# print("Outside the loop.",counter)

#for loop
# for counter in range(10):
#     print("Counter:",counter)

# for counter in range(1000):
#     print("Counter:",counter)
# for counter in range(2,8):
#     print("Counter:",counter)

# largest_number=-99999999
# counter=0

# while True:
#     number =  int(input("Enter a number or type -1 to stop:"))
#     if number==-1:
#         break
#     counter+=1
#     if number> largest_number:
#        largest_number=number

# if counter!=0:
#     print("The largest number  is:",largest_number)
# else:
#     print("You haven't entered any number.")

# largest_number=-99999999
# counter=0
# number=int(input("Enter a number or type -1 to end program:"))
# while number!=-1:
#     # if number==-1:
#     #     continue
#     counter+=1

#     if number>largest_number:
#         largest_number=number
#     number =  int(input("Enter a number or type -1 to stop:"))

# if counter:
#     print("The largest number is : ",largest_number)
# else:
#     print("You haven't entered any number")

# counter=1
# while counter<5:
#     print(counter)
#     counter+=1
# else:
#     print("else:",counter)


# counter=5
# while counter<5:
#     print(counter)
#     counter+=1
# else:
#     print("else:",counter)


# for counter in range(5):
#     print(counter)
# else:
#     print("Else:",counter)

# counter=111
# for counter in range(2,1):
#     print(counter)
# else:
#     print("Else:",counter)

# blocks=int(input("Enter the number of blocks:"))
# counter=0
# height=0

# while (blocks -counter>0):
#     counter+=1
#     blocks=blocks-counter

# print("Height of the pyramid:",counter)
# print(f'Height of the pyramid:{counter}qifeb{blocks}')

#18/06/2026

# #lists
#numbers=[]    #reading
# numbers=[10,5,7,2,1]  #reading and initialization

# print(numbers)
# print(type(numbers))
# #accessing list elements
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# print(numbers[5])

# numbers[0]=100  #writing an element
# print(numbers)

#19/06/2026  Friday
# numbers=[10,5,7,2,1]
# print("Original list contents:",numbers)#Printing original list contents
# numbers[0]=111
# print("New list  contents:",numbers)  #Current list contents 

# print("Original list contents:",numbers)  #Printing original list contents 
# numbers[1]=numbers[4]  #copying value of the fifth element to the second
# print("New list  contents:",numbers)  #Printing current list contents

# print(numbers)
# print(len(numbers))

# del numbers[1]

# print(numbers)
# print(len(numbers))

#negative indexing in lists
# numbers=[111,7,2,1]
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-4])
# print(numbers[len(numbers)*-1])

# hat=[1,2,3,4,5]

# print(len(hat))

# del hat[len(hat)-1]
# print(hat)
# user=int(input("Enter a number:"))
# hat[int(len(hat)//2)]=user  #floor division
# print(hat)

#22/06/2026   Monday

# list functions
# print([1,2]+[3])

#append()
# list=[5,4,3,2,1]
# print(list)
# print(f'Length of List:{len(list)}')
# list.append(6)
# print(list)
# print(f'Length of List:{len(list)}')

#insert(ind,element)
# numbers=[111,7,2,1]
# print(len(numbers))
# print(numbers)

# numbers.append(4)
# print(len(numbers))
# print(numbers)

# numbers.insert(0,222)
# print(len(numbers))
# print(numbers)

#traversal & iteration

# list1=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list1)):
#     print(list1[i])

# list=[]
# for i in range(1,11):
#     # list.insert(i,i+1)
#     list.append(i)
# print(list)

# list=[]
# count=1
# while count<=10:
#     list.append(count)
#     count+=1
# print(list)

# list=[10,20,30,40,50,60,70,80,90,100]
# for i in range(10):
#     list[i]+=1
# print(list)

#24/06/2026  Wednesday

# my_list=[10,20,30,40,50,60,70,80,90,100]
# #Print the sum of all the elements from the list
# sum=0
# # for i in range(len(my_list)):
# #     sum+=my_list[i]
# for element in my_list:
#     sum+=element
# print("Sum:",sum)

#copying a variable into another variable
# a=10
# b=20
# print("a:",a)
# print("b:",b)

# a,b=b,a

# print("a:",a)
# print("b:",b)

# my_list=[10,1,8,3,5]
# print(my_list)
# my_list[0],my_list[4]=my_list[4],my_list[0]
# my_list[1],my_list[3]=my_list[3],my_list[1]
# print(my_list)

# bubble sort
# take two adjacent elments
# if 1st element is greater then second swap otherwise move ahead

#25/06/2026  Thursday

#BUBBLE SORT

# my_list=[8,10,6,2,4]
# print(my_list)
# count=0
# for index1 in range(len(my_list)-1):
#     # for index in range(len(my_list)-1):
#     for index in range(len(my_list)-1-index1):   #efficient case
#         count+=1
#         if my_list[index] > my_list[index+1]:
            
#             my_list[index] , my_list[index+1] = my_list[index+1] , my_list[index]
# print(my_list)
# print("My run has run for:",count,"times")

#ASSIGNMENT PROBLEM 1
'''
Practice Question
The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
step 1: create an empty list named beatles;step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;step 5: use the insert() method to add Ringo Starr to the beginning of the list.
'''
# beatles=[]
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print(beatles)

# user=["Stu Sutcliffe","Pete Best"]
# i=0
# for i in range(2):
#     beatles.append(user[i])

# print(beatles)

# del beatles[len(beatles)-1]
# del beatles[len(beatles)-1]
# print(beatles)

# beatles.insert(0,"Ringo Starr")
# print(beatles)

#26/06/2026   Friday
# my_list=[8,10,6,2,4]
# swapped=True     #It's a little fake,we need it to enter the while loop
# count=0
# while swapped:
#     swapped=False  #no swaps so far
#     for i in range(len(my_list)-1):
#         count+=1
#         if my_list[i] > my_list[i+1]:
#             swapped=True  #a swap occured
#             my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
# print(my_list)
# print("Loops are running for:",count,"times")

'''
'''


# my_list=[1,2,3,4,5]  #already sorted (best case)
# swapped=0
# print(my_list)
# count=0
# for index1 in range(len(my_list)-1):
#     # for index in range(len(my_list)-1):
#     for index in range(len(my_list)-1-index1):   #efficient case
#         count+=1
#         if my_list[index] > my_list[index+1]:
            
#             my_list[index] , my_list[index+1] = my_list[index+1] , my_list[index]
#             swapped=1
#         if swapped==0:
#             break

# print(my_list)
# print("My run has run for:",count,"times")  #4 times

# my_list=[8,10,6,2,4]
# print(my_list)
# my_list.sort()
# print(my_list)

# lst=[5,3,1,2,4]
# print(lst)
# lst.reverse()
# print(lst)

'''
logic
length=x
[a,b,c,d,e,f,g]
[g,f,e,d,c,b,a]

0- -1
1- -2 
-1*(index+1
)'''

# #Reversing the order of list
# lst=[5,3,1,2,4]
# print(len(lst)//2)
# print(lst)
# for i in range(len(lst)//2):  #i for index
#     # lst[i],lst[(-1)*(i+1)]=lst[(-1)*(i+1)],lst[i]
#     lst[i],lst[len(lst)-(i+1)]=lst[len(lst)-(i+1)],lst[i]
# print(lst)

#29/06/2026   Monday

# lst=["D","F","Z","a"," "]
# lst.sort()
# print(lst)

# print("B">"b")

# a=3
# b=1
# c=2
# lst=[a,c,b]
# lst.sort()
# print(lst)

# a="A"
# b="B"
# c="C"
# d=" "
# lst=[a,b,c,d]
# lst.reverse()
# print(lst)

# lst_1=[1]
# lst_2=lst_1   #reference copy
# lst_1[0]=2
# print(lst_2)

# lst_1=[1,2,3,4]
# lst_2=lst_1[0:2]
# lst_1[0]=2
# print("List1:",lst_1)
# print("List2:",lst_2)

# my_list=[10,8,6,4,2]
# new_list=my_list[1:3]
# print(new_list)

# new_list=my_list[1:-1]
# print(new_list)

# new_list=my_list[-1:1]
# print(new_list)

# print(ord("A"))     Ascii value

#30/06/2026  Tuesday

# my_list=[10,8,6,4,2]
# del my_list
# print(my_list)

# my_list=[0,3,12,8,2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# lst = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest=lst[0]
# for i in range(1,len(lst)):
#     if lst[i]>largest:
#         largest=lst[i]

# print("largest no.",largest)

# lst = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest=0
# for i in range(len(lst)):
#     if largest < lst[i]:
#         largest=lst[i]
# print("Largest no. ",largest)

# lst = [ 17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest=lst[0]
# for element in lst:
#     if largest < element :
#         largest=element
# print("Largest no. ",largest)

# my_list=[17,3,11,5,1,9,7,15,13]
# for i in range(len(my_list)):
#     if my_list[i]==5:
#         print("element 5 is found at:",i)
#         break

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# found = -1
# for i in range(len(my_list)):
#     if my_list[i] == 5:
#         found = i
#         break
# if found != -1:
#     print("5 found at index:", found)
# else:
#     print("5 not found")

# list_1=["A","B","C"]
# list_2=list_1
# list_3=list_2
# del list_1[0]
# del list_2[0]
# print(list_3)

# list_1=["A","B","C"]
# list_2=list_1
# list_3=list_2
# del list_1[0]
# del list_2
# print(list_3)

# list_1=["A","B","C"]
# list_2=list_1
# list_3=list_2
# del list_1[0]
# del list_2[:]
# print(list_3)


# list_1=["A","B","C"]
# list_2=list_1[:]
# list_3=list_2[:]
# del list_1[0]
# del list_2[0]
# print(list_1)
# print(list_2)
# print(list_3)


#15/07/2026   Wednesday

#List Comprehension
#row=[]
# for i in range(8):
#     row.append("WHITE_PAWN")

# row=["WHITE_PAWN" for i in range(8)]
# print(row)

# squares=[x**2 for x in range(10)]
# print(squares)

# # twos=[2**i for i in range(8)]
# # print(twos)

# odds=[x for x in squares if x%2!=0]
# print(odds)

# even=[x for x in squares if x%2==0]
# print(even)

# board=[]
# for i in range(8):
#     row=["EMPTY" for i in range(8)]
#     board.append(row)
# print(board)

# board[0][0]='ROOK'
# board[0][7]='ROOK'
# board[7][0]='ROOK'
# board[7][7]='ROOK'

# board[0][1]='KNIGHT'
# board[0][6]='KNIGHT'
# board[7][1]='KNIGHT'
# board[7][6]='KNIGHT'

# board[0][2]='BISHOP'
# board[0][5]='BISHOP'
# board[7][2]='BISHOP'
# board[7][5]='BISHOP'

# for index in range(len(board)):
#     print(board[index])

# temps=[[0.0 for h in range(24)] for d in range(31)]
# #print(temps)
# random=[35,23,26,38,12,35,23,26,38,12,35,23,26,38,12,35,23,26,38,12,35,23,26,38,12,35,23,26,38,12,10]
# for index in range(len(temps)):
#     temps[index][11]=random[index]

# for index in range(len(temps)):
#     print(temps[index])
# sum=0
# for index in range(len(temps)):
#     sum+=temps[index][11]
# print("Average temperature:",sum/31)
# highest_temp=-100
# for index in range(len(temps)):
#     for inner_index in range(len(temps[index])):
#         if highest_temp<temps[index][inner_index]:
#             highest_temp =temps[index][inner_index]
# print(highest_temp)

# lowest=100

# for index1 in range(len(temps)):
#     for inner_index in range(len(temps[index1])):
#         if lowest>temps[index1][inner_index]:
#             lowest=temps[index1][inner_index]
# print(lowest)

rooms=[[[False for r in range(20)] for f in range(15)] for b in range(3)]
print(len(rooms))
for building_index in range(len(rooms)):
    print("Building:",building_index+1)
    for floor_index in range(len(rooms[building_index])):
        print("Floor:",floor_index+1)
        print(rooms[building_index][floor_index])


























                    






    



