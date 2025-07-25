def count_the_vowels(str):
    count=0
    for i in str:
        if i in "aeiou" or i in "AEIOU":
            count=count+1
    return count
