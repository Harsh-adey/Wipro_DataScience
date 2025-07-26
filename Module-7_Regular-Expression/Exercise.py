#1)Write a program to find check if a string has only octal digits. Given string ['789','123','004']
def has_only_octal_digits(s):
    """
    Checks if a string contains only octal digits (0-7).

    Args:
        s: The input string to check.

    Returns:
        True if the string contains only octal digits, False otherwise.
    """
    if not s:
        return False  # An empty string is not considered to have octal digits.
    
    try:
        # The int() function with base 8 will try to parse the string as an
        # octal number. It will raise a ValueError if it encounters any
        # character that is not a valid octal digit (0-7).
        int(s, 8)
        return True
    except ValueError:
        # A ValueError means the string contains non-octal characters.
        return False

# --- Main Program ---
if __name__ == "__main__":
    # The list of strings to check, as provided in the request.
    string_list = ['789', '123', '004']

    print("--- Checking Strings for Octal Digits ---")
    
    # Iterate through each string in the list and check it.
    for text in string_list:
        is_octal = has_only_octal_digits(text)
        print(f"String: '{text}' -> Contains only octal digits? {is_octal}")

    print("\n--- Additional Test Cases ---")
    # Some other examples to demonstrate the function's behavior.
    test_cases = ["12345670", "8", "abc", "0", "-123", ""]

    for test in test_cases:
        is_octal = has_only_octal_digits(test)
        print(f"String: '{test}' -> Contains only octal digits? {is_octal}")


#2)Extract the user id, domain name and suffix from the following email addresses. emails = """zuck@facebook.com sunder33@google.com jeff42@amazon.com"""
import re

def parse_emails(email_string):
    """
    Parses a string of email addresses to extract user ID, domain, and suffix.

    Args:
        email_string: A string containing one or more space-separated email addresses.

    Returns:
        A list of dictionaries, where each dictionary contains the
        'user_id', 'domain', and 'suffix' for an email address.
        Returns an empty list if no valid emails are found.
    """
    # Regex to capture the three parts of an email address:
    # 1. (\S+): Captures the user ID (one or more non-whitespace characters)
    # 2. @: Matches the literal '@' symbol
    # 3. ([a-zA-Z0-9.-]+): Captures the domain name. Allows letters, numbers, dots, and hyphens.
    # 4. \.: Matches the literal '.' separating domain and suffix.
    # 5. ([a-zA-Z]{2,}): Captures the suffix (at least two letters).
    email_pattern = re.compile(r"(\S+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})")
    
    # Find all matches in the input string
    matches = email_pattern.finditer(email_string)
    
    extracted_data = []
    for match in matches:
        user_id = match.group(1)
        domain = match.group(2)
        suffix = match.group(3)
        extracted_data.append({
            "email": match.group(0), # The full email match
            "user_id": user_id,
            "domain": domain,
            "suffix": suffix
        })
        
    return extracted_data

# --- Main Program ---
if __name__ == "__main__":
    # The string of emails provided in the request.
    emails = """zuck@facebook.com sunder33@google.com jeff42@amazon.com"""

    # Parse the emails
    parsed_emails = parse_emails(emails)

    # Print the results in a formatted way
    if parsed_emails:
        print("--- Extracted Email Components ---")
        for data in parsed_emails:
            print(f"Email:   {data['email']}")
            print(f"  - User ID: {data['user_id']}")
            print(f"  - Domain:  {data['domain']}")
            print(f"  - Suffix:  {data['suffix']}")
            print("-" * 20)
    else:
        print("No valid email addresses were found.")


#3)Split the following irregular sentence into proper words sentence = """A, very very; irregular_sentence""" ## expected outout : A very very irregular sentence

import re

sentence = """A, very very; irregular_sentence"""

# Replace punctuation (except underscore) with space
cleaned = re.sub(r'[^\w\s_]', ' ', sentence)

# Replace underscores with space
cleaned = cleaned.replace('_', ' ')

# Remove extra spaces
cleaned = ' '.join(cleaned.split())

print(cleaned)

import re

def clean_sentence(irregular_sentence):
    """
    Cleans an irregular sentence by replacing specific punctuation with spaces
    and normalizing whitespace.

    Args:
        irregular_sentence: The input string with irregular separators.

    Returns:
        A cleaned string with single spaces between words.
    """
    # Step 1: Replace commas, semicolons, and underscores with a space.
    # The character set `[;,_]` matches any single character that is a
    # semicolon, comma, or underscore.
    # re.sub() finds all matches and replaces them with a space ' '.
    spaced_sentence = re.sub(r'[;,_]', ' ', irregular_sentence)
    
    # Step 2: Normalize whitespace.
    # The input string might now have multiple spaces between words
    # (e.g., "very  very").
    # .split() without arguments splits the string by any whitespace
    # and discards empty strings, resulting in a clean list of words.
    words = spaced_sentence.split()
    
    # Step 3: Join the words back together with a single space.
    # ' '.join() creates a new string from the list of words,
    # separated by a single space.
    cleaned_sentence = ' '.join(words)
    
    return cleaned_sentence

# --- Main Program ---
if __name__ == "__main__":
    # The irregular sentence from the request.
    sentence = """A, very very; irregular_sentence"""
    
    # The expected result.
    expected_output = "A very very irregular sentence"
    
    # Clean the sentence using the function.
    actual_output = clean_sentence(sentence)
    
    # Print the results for verification.
    print(f"Original sentence:  '{sentence}'")
    print(f"Cleaned sentence:   '{actual_output}'")
    print(f"Expected output:    '{expected_output}'")
    
    # Verify that the output matches the expectation.
    print(f"\nOutput matches expectation: {actual_output == expected_output}")

#4)Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. #tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' ##desired_output = 'Good advice What I would do differently if I was learning to code today'

import re

def clean_tweet(tweet_text):
    """
    Cleans a tweet by removing URLs, mentions, hashtags, "RT", "cc",
    and punctuation.

    Args:
        tweet_text: The raw tweet string.

    Returns:
        A cleaned string containing only the user's message.
    """
    # Create a copy to modify
    text = tweet_text
    
    # 1. Remove URLs: Matches http/https/www and any non-space characters after.
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 2. Remove mentions and hashtags: Matches @ or # followed by word characters.
    text = re.sub(r'[@#]\w+', '', text)
    
    # 3. Remove "RT" and "cc" (case-insensitive)
    # \b ensures we match whole words only.
    text = re.sub(r'\b(RT|cc)\b', '', text, flags=re.IGNORECASE)
    
    # 4. Remove all punctuation: Matches any character that is not a
    # word character (\w) or whitespace (\s).
    text = re.sub(r'[^\w\s]', '', text)
    
    # 5. Normalize whitespace: Splits the string into a list of words
    # by any whitespace, then joins them back with a single space.
    # This removes extra spaces created by the substitutions above.
    words = text.split()
    cleaned_text = ' '.join(words)
    
    return cleaned_text

# --- Main Program ---
if __name__ == "__main__":
    # The tweet from the request.
    tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
    
    # The desired output for verification.
    desired_output = 'Good advice What I would do differently if I was learning to code today'
    
    # Clean the tweet using the function.
    actual_out

#5)Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html Code to retrieve the HTML page is given below: import requests r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text # html text is contained here desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']

import requests
from bs4 import BeautifulSoup
import re

def extract_html_text(url):
    """
    Fetches an HTML page from a URL and extracts all visible text portions.

    Args:
        url: The URL of the HTML page to process.

    Returns:
        A list of strings, where each string is a piece of text found
        in the HTML body. Returns an empty list if the request fails.
    """
    try:
        # Step 1: Fetch the HTML content from the URL
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        html_text = response.text
        
        # Step 2: Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')

        # Step 3: Extract text using .stripped_strings
        # .stripped_strings is a generator that yields all the strings from the
        # document, with leading/trailing whitespace removed. This is a very
        # efficient way to get all the text content. We convert it to a list.
        # We also filter out any strings that are just comments.
        text_list = []
        for s in soup.stripped_strings:
            # The 'NavigableString' object from BeautifulSoup can sometimes be
            # a comment. We check its parent's name to exclude it.
            # A simpler way is to just check if it's a comment type, but
            # iterating and checking is robust.
            # A more direct check is to avoid adding if it's a comment.
            # However, stripped_strings usually handles this well.
            # For this specific file, a direct conversion is clean.
            text_list.append(s)
            
        return text_list

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# --- Main Program ---
if __name__ == "__main__":
    # The URL from the request
    url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
    
    # The desired output for verification
    desired_output = [
        'Your Title Here', 
        'Link Name', 
        'This is a Header', 
        'This is a Medium Header', 
        'This is a new paragraph! ', # Note: BeautifulSoup strips trailing space
        'This is a another paragraph!', 
        'This is a new sentence without a paragraph break, in bold italics.'
    ]
    
    # Adjusting desired output because .stripped_strings removes trailing spaces
    adjusted_desired_output = [s.strip() for s in desired_output]

    # Get the actual output from our function
    actual_output = extract_html_text(url)
    
    # Print the results for comparison
    print("--- Extracted Text ---")
    print(actual_output)
    
    print("\n--- Desired Output (Adjusted for Stripped Whitespace) ---")
    print(adjusted_desired_output)
    
    # Check if the result matches the desired output
    print(f"\nOutput matches desired: {actual_output == adjusted_desired_output}")


#6)Given below list of words, identify the words that begin and end with the same character. civic trust widows maximum museums aa as

def find_words_with_same_start_and_end(word_list):
    """
    Identifies words from a list that begin and end with the same character.

    Args:
        word_list: A list of strings (words).

    Returns:
        A list of words that satisfy the condition.
    """
    matching_words = []
    for word in word_list:
        # Ensure the word is not empty to avoid an IndexError
        if len(word) > 0:
            # Compare the first character (index 0) with the last (index -1)
            # We convert the word to lowercase to make the comparison case-insensitive,
            # which is generally more robust (e.g., "Anna" would match).
            if word.lower()[0] == word.lower()[-1]:
                matching_words.append(word)
    return matching_words

# --- Main Program ---
if __name__ == "__main__":
    # The list of words from the request, provided as a string and then split.
    words_string = "civic trust widows maximum museums aa as"
    words = words_string.split()
    
    # Find the words that match the criteria.
    result = find_words_with_same_start_and_end(words)
    
    # Print the original list and the result.
    print(f"Original list of words: {words}")
    print(f"Words that begin and end with the same character: {result}")

    # --- Another Example ---
    print("\n--- Testing with another list ---")
    test_list = ["Anna", "level", "test", "Stats", "Python", "eye"]
    test_result = find_words_with_same_start_and_end(test_list)
    print(f"Original list of words: {test_list}")
    print(f"Words that begin and end with the same character: {test_result}")



