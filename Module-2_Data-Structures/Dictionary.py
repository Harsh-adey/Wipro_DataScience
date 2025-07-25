"""Write a program to add a key and value to a dictionary."""

dict={0:10,1:20}
print(dict)
dict[2]=30
print(dict)

"""Write a program to concatenate the folloeing dictionaries to create a new one"""

dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}

result={**dict1,**dict2,**dict3}
print(result)

"""Write a program to check if a given key already exists in a dictionary. """

dict4={1:10,2:20,3:30,4:40,5:50,6:60}
k=int(input("Enter a key you want to check: "))
key_list=list(dict4.keys())
if k in key_list:
   print(f"The key {k} is present.")
else:
   print(f"The key {k} is not present.")

""" Write a program to iterate over a dictionary using for loop """

dict5={1:10,2:20,3:30,4:40,5:50,6:60}
for i in dict5:
   print(i,end=" ")
print()
for j in dict5:
   print(dict5[j],end=" ")
print()
for k in dict5:
   print(k,":",dict5[k])


"""Write a program to prepare a dictionary where the keys are numbers between
1 and 15 (both included) and the values are square of the keys."""

dict6={}
for i in range(1,16):
     dict6[i]=i*i
print(dict6)

"""Write a program to sum all the values in a dictionary,
considering the values will be of int type."""

dict7={'a':1,'b':2,'c':3,'d':4}
sum1=0
for i in dict7:
   sum1=sum1+dict7[i]
print(sum1)
