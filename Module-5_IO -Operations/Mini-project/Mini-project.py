"""Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.

Hints to find the secret message:

1. The number of lines in the file tells you the meeting time.

Note: 1<= number of lines <= 24

If the number of lines is exceeding 12, you need to convert it to 12 hour

format. For example,

If the number of lines is 15, then the meeting time is 3 PM.

If the number of lines is 10, then the meeting time is 10 AM.

2. The word appearing for the maximum number of times tells you the meeting place.

Note: Meeting place will be a street name."""

def meeting_time(data):
    if len(data)>12:
       print("Meeting time is ",len(data)-12,"PM")
    else:
       print("Meeting time is",len(data),"AM")

def meeting_place(dict):
    most_time=max(dict,key=dict.get)
    return most_time

with open("io.txt",'r') as file:
    text=file.read().lower()
    words=text.split()
    stop_words = ["the", "on", "of", "is", "a", "an", ","]
    dict={}
    for word in words:
        if word not in stop_words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

with open("io.txt", 'r') as file:
    data = [line.strip() for line in file]

get_meeting_time(data)
Ans=get_meeting_place(dict)
print("The place of meeting is:",Ans,"street")
