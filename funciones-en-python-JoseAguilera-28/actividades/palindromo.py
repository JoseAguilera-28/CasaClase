def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

print(is_palindrome("Anita lava la tina"))
print(is_palindrome("Python"))
print(is_palindrome("A man a plan a canal Panama"))
