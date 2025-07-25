"""Write a program to print the 4th element from first and 4th element from last in a tuple."""

tup=(1,2,3,4,5,6,7)
if len(tup)>4:
   b=int(input("Enter the element"))
   print(tup[b-1],tup[-b])
else:
   print("No elements.")

"""Write a program to check whether an element exists in a tuple or not."""
tup1=(1,2,3,4,5,6,6,7,23,4)
a1=int(input("Enter a number : "))
for i in tup1:
   if a1==i:
      print(f"The number {a1} exist")
      break
   else:
      print(f"The number {a1} not exist")

"""Write a program to convert a list into a tuple."""
lis1=(1,2,3,4,5,5,3)
lis1=tuple(lis1)
print(type(lis1))

"""Write a program to find the index of an item in a tuple."""

tup2=(1,2,3,4,5,5,3)
a2=int(input("Enter the number: "))
if a2 in tup2:
   print(tup2.index(a2))

"""Write a program to replace last value of tuples in a list to 100"""
list2=[(10,20,30),(40,50,60),(70,80,90)]
list3=[]
for i in list2:
   list3.append(list(i))
for i in list3:
   i[-1]=100
print(list9)
