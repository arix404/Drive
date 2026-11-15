import random
import string

captcha= ''.join(random.choices(string.ascii_letters+string.digits, k=6))

print ("Captcha: ", captcha)

user = input("Enter the captcha: ")

if user==captcha:
    print("valid captcha")
else:
    print("invalid captcha")