def is_palindrome(str):
   start=0
   end=len(str)-1
   while start<end:
      if str[start]!=str[end]:
         return False
      start=start+1
      end=end-1
   return True
