def is_palindrome(text):
    result=text.replace(" ","")
    result=result.lower()
    if result==result[::-1]:
        return "True"
    else:
        return "False"
print(is_palindrome('level'))
print(is_palindrome('Hello'))
print(is_palindrome('racecar'))
print(is_palindrome('A man a plan a canal panama'))