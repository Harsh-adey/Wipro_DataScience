"""Through command line arguments three strings seperated by space are given to you.
Each string is a series of numbers seperated by hyphen(-). You like allnumbers in string 1 and dislike all
numbers in string 2.

Thrid string contains the numbers given to you. Your initial happiness is 0.
When you encounter a number which is present in string 1,add 1 to your happiness, if it is present in string 2,
add -1 to your happiness. Otherwise  your happiness does not change.
Output your final happiness at the end."""

import sys

def count_happiness(str1,str2,str3):
    l1=list(map(int,str1.split("-")))
    l2=list(map(int,str2.split("-")))
    l3=list(map(int,str3.split("-")))
    count=0
    for i in l3:
        if i in l1:
            count=count+1
        elif i in l2:
            count=count-1
    return count


s1 = sys.argv[1]
s2 = sys.argv[2]
s3 = sys.argv[3]
Ans = count_happiness(s1, s2, s3)
print(" Score:", Ans)
