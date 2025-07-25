""" Write a function to return the sum of all numbers in a list.  
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""

def sum(li):
    sum1=0
    for i in li:
        sum1=sum1+i
    return sum1

li=list(map(int,input().split(" ")))
Ans=sum_li(li)
print("The sum = ",Ans)

""" Write a function to return the reverse of a string.  
Sample String : "1234abcd"
Expected Output : "dcba4321" """

def rev_str(str):
    return str[::-1]
str=input("Enter a string: ")
Ans1=rev_str(Ans1)
print(Ans1)

"""Write a function to calculate and return the factorial of a numner"""

def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)

num=int(input("Enter a number: "))
Ans2=fact(num)
print(f"The factorial of number {num}  is {Ans2}")

"""Write a function that accepts a string and prints the number of
upper case letters and lower caseletters in it."""

def count_up_lo(str1):
    up=0
    low=0
    for i in str1:
       if i.isupper():
          up=up+1
       else:
          low=low+1
    return up,low

str2=input("Enter a string ")
Ans2=count_up_lo(str2)
print(f"The upper case letters are {Ans2[0]} and lowercase letters are {Ans2[1]}")

"""Write a function to print the even numbers from a given list.
List is passed to the function as an argument."""

def even_li(li1):
    li2=[]
    for i in li1:
        if i%2==0:
            li2.append(i)
    return li2

li3=list(map(int,input().split(" ")))
print(even_li(li3))

"""Write a function that takes a number as a parameter
and checks the number is prime or not"""

def is_prime(num1):
    for i in range(2,num1//2):
        if num1%i==0:
            return False
    return True

num1=int(input("Enter a number: "))
print("The number is prime:",is_prime(num1))
