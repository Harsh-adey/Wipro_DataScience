"""Write a program to create a list of 5 integers and display
the list items.Access individual elements through index. """

l1=[1,2,3,4,5]
for i in range(len(l1)):
   print(l1[i])

"""Write a program to append a new item to the end of the list"""

l2=[1,2,3,4]
l2.append(5)
print(l2)

"""Write a program to reverse the order of the items in the list"""

l3=[5,4,3,2,1]
l3.reverse()
print(l3)

"""Write a program to print the number of occurrences of a specified element in a list."""
l4=[4,4,3,2,4,1,2]
c=int(input("Enter a number to count: "))
b=l4.count(c)
print(f"The number {c} occurr {b} times")
      
"""Write a program to append the items of list1 to list2 in the front"""
l5=[4,5,6]
l6=[1,2,3]
l5=l6+l5
print(l5)
   
"""Write a program to remove the item from a specified index in a list"""
l7=[1,2,3,4,5]
l7.pop(2)
print(l7)

"""Write a program to insert a new item before the element in an existing list."""

l8=[1,3,4,5]
l8.insert(1,2)
print(l8)

"""Write a program to remove the  first occurrence of  a specified element in a list"""

l9=[1,4,3,4,5,6,4]
g=int(input("Enter the element you want to remove: "))
if g in l9:
   l9.remove(g)
print(l9)
