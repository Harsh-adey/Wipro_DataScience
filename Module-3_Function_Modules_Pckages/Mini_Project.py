"""Write a python function that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-seperated sequence after sorting
them alphabatically."""


def color_sort(string):
    list=string.split("-")
    list.sort()
    string2="-".join(list)
    return string2
    
string=input("Enter colors separated by hyphen ").lower()
Ans=color_sort(string)
print(Ans)
