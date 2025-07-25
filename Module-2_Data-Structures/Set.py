"""Write a program to remove a given item from the set. """

set1={1,2,34,5,23}
i=int(input("Enter the number you want to remove: "))
if i in set1:
   set1.remove(2)
   print(set1)
else:
   print("The element is not in the set")

"""Write a program to create an intersection of sets."""

set2={1,2,34,5,6,323,90}
set3={34,5,6,2,80,70}
print(set2.intersection(set3))


"""Write a program to create an union of sets."""

set2={1,2,34,5,6,323,90}
set3={34,5,6,2,80,70}
print(set2.union(set3))

"""Write a program to find the maximum and minimum value in the set"""

set2={1,2,34,5,6,323,90}
print("The maximum value=",max(set2))
print("The minmum value=",min(set2))
