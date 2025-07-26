#1)Write a program to find check if a string has only octal digits. 
#Given string ['789','123','004']

string_list = ['789', '123', '004']

# Function to check if a string has only octal digits
def is_octal(s):
    for char in s:
        if char not in '01234567':
            return False
    return True

# Check each string in the list
for s in string_list:
    if is_octal(s):
        print(f"'{s}' contains only octal digits.")
    else:
        print(f"'{s}' does NOT contain only octal digits.")




#2)Extract the user id, domain name and suffix from the following email addresses. 
#emails = """zuck@facebook.com sunder33@google.com jeff42@amazon.com"""

import re

emails = "zuck@facebook.com sunder33@google.com jeff42@amazon.com"

# Regular expression to extract user ID, domain, and suffix
pattern = r'([\w\.]+)@([\w\.]+)\.(\w+)'

# Find all matches
matches = re.findall(pattern, emails)

# Print the extracted components
for user, domain, suffix in matches:
    print(f"User ID: {user}, Domain: {domain}, Suffix: {suffix}")

        

#3)Split the following irregular sentence into proper words sentence = """A, 
#very very; irregular_sentence""" ## expected outout : A very very irregular sentence

import re

sentence = """A, 
very very; irregular_sentence"""

# Replace non-word characters (except space) with space, then normalize whitespace
cleaned = re.sub(r'[^\w\s]', ' ', sentence)        # Replace punctuation with space
cleaned = re.sub(r'_', ' ', cleaned)               # Replace underscores with space
cleaned = re.sub(r'\s+', ' ', cleaned).strip()     # Remove extra spaces

print(cleaned)

#4)Clean up the following tweet so that it contains only the user’s message. 
#That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. #tweet = '''Good advice! RT @TheNextWeb: What I would do 
#differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' ##desired_output = 'Good advice 
#What I would do differently if I was learning to code today'
import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

# Step-by-step cleaning
tweet = re.sub(r'RT\s+', '', tweet)                     # Remove RT
tweet = re.sub(r'cc:', '', tweet)                       # Remove cc
tweet = re.sub(r'http\S+', '', tweet)                   # Remove URLs
tweet = re.sub(r'@\w+', '', tweet)                      # Remove mentions
tweet = re.sub(r'#\w+', '', tweet)                      # Remove hashtags
tweet = re.sub(r'[^\w\s]', '', tweet)                   # Remove punctuations
tweet = re.sub(r'\s+', ' ', tweet).strip()              # Normalize whitespace

print(tweet)



#5)Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.
#html Code to retrieve the HTML page is given below: import requests r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text 
# html text is contained here desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 
#'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']


import requests
from bs4 import BeautifulSoup

# Fetch HTML
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract all text contents, ignoring scripts/styles
text_elements = [element.strip() for element in soup.stripped_strings]

print(text_elements)


#6)Given below list of words, identify the words that begin and end with the same character. civic trust widows maximum museums aa as

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

# Filter words that start and end with the same character
matching_words = [word for word in words if word[0].lower() == word[-1].lower()]

print(matching_words)
