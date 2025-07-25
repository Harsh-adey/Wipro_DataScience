""" Write a program to accept two numbers from the user and perform division. If any exception occurs,
 print an error message or else print the result."""

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Zerodivision error occurs")
except ValueError:
    print("You enter wrong value.")


""" Write a program to accept a number from the user and check whether it’s prime or not.
 If user enters anything other than number, handle the exception and print an error message."""

def is_prime(num):
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True

try:
    num=int(input("Enter a number: "))
    res=is_prime(num)
    print(f"The number {num} is prime=",res)
except ValueError:
    print("You enter wrong value.")

"""Write a program to accept the file name to be opened from the user, 
if file exist print the contents of the file in title case or else handle the exception and print an error message."""

try:
    filename=input("Enter the file name: ")
    with open(filename,'r') as file:
        text=file.read()
        print(text.title())
except FileNotFoundError:
    print("File not exist")


"""Declare a list with 10 integers and ask the
 user to enter an index. Check whether the number in that 
 index is positive or negative number. If any invalid index 
 is entered, handle the exception and print an error message."""

li=[1,23,-4,-41,3435,657,-85,436,77,-3]

try:
    f=int(input("Enter the index you want to check"))
    if li[f]<0:
        print("The number is negative")
    elif li[f]>0:
        print("The number is positive.")
    else:
        print("The number is 0.")
except ValueError:
    print("You enter the wrong value.")
except IndexError:
    print("Error: Invalid index. Please enter a number between 0 and 9.")
 
