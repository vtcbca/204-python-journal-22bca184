#Write a script to enter any word and check it is palindrom or not.

p = input("Enter a word: ")
if p == p[::-1]:
    print(f"{p} is a palindrome.")
else:
    print(f"{p} is not a palindrome.")
