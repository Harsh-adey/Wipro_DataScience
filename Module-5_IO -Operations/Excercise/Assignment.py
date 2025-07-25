"""Write a program to read the entire content from a txt file and display it to the user."""

with open("IO.txt",'r') as file:
    text=file.read()

print(text)

"""Write a program to read first n lines from a txt file. Get n as user input."""

def read_n_lines(n):
    with open("IO.txt",'r') as file:
          for i in range(n):
              lines=file.readline()
              if lines == "":
                    print("File has fewer than", n, "lines.")
                    break
              print(lines.strip()) 
m=int(input("Enter the number: "))
read_n_lines(m)

""" Write a program to accept input from user and append it to a txt file."""

wor=input("Enter the string=")
with open("test.txt",'a') as file1:
    file1.write(wor)

""" Write a program to read contents from a txt file line by line and store each line into a list"""

with open("io.txt",'r') as file2:
    lines=[line.strip() for line in file2]
    print(lines)

"""Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it."""

def longest_word(dict1):
    return max(dict1,key=len)

with open("test.txt",'r') as file:
    text=file.read().lower()
    words=text.split()
    dict1={}
    for word in words:
        if word not in dict1:
            dict1[word] = len(word)

o=longest_word(dict1)
print(o)

"""Write a program to count the frequency of a user entered word in a txt file."""

def frequency_word(str1):
    with open("io.txt",'r') as file1:
        text1=file1.read().lower()
        words1=text1.split()
        count=0
        for word in words1:
                if str1==word:
                    count =count+ 1
    return count

str1=input("Enter the string=")
Ans=frequency_word(str1)
print(Ans)
