"""Write a program to count the number of upper and lower case letters in a string."""

str="Hello World"
up=0
low=0
for i in str:
   if i.isupper():
      up=up+1
   else:
      low=low+1
print(f"The uppercase letters are {up} and lower case letters are {low}.")


"""Write a program that will checck whether a given string is palindrome or not."""
def is_palindrome(str1):
   start=0
   end=len(str1)-1
   while start<end:
      if str1[start]!=str1[end]:
         return False
      start=start+1
      end=end-1
   return True

str1=input("Enter a string=")
Ans=is_palindrome(str1)
print(f"The given string is palindrome: {Ans}")

"""Given a string, return a new string made of n copies of the first 2
   chars of the original string where n is the length of the string. The 
   string length will be >=2. If the input is Wipro then output sholud be
   WiWiWiWiWi."""

str2=input("Enter a string: ")
n=len(str2)
print(str20:2]*n)

"""Given a string , if the first or last character is 'x' , return 
the string without those 'x' character, else return the string unchanged.
If the input is "xHix" ,then output is "Hi" """

str3=input("Enter a string: ")
if str3[0]=='x' and str3[-1]=='x':
   print(str3[1:-1])
else:
   print(str3)

"""Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
 You may assume that n is between 0 and the length of the string inclusive. 
 For example if the inputs are “Wipro” and 3, then the output should be “propropro”."""

def last_char(str4,f):
   return (str4[-(f):]*f)
str4=input("Enter a string: ")
f=int(input("Enter a number beyween 0 and len of str4: "))
Ans=last_char(str4,f)
print(Ans)
