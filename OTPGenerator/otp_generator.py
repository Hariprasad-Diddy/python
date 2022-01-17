import random

def otp():
    # Randomly generating 6 digits of OTP 
    a = random.randint(111111,999999)
    # printing the output
    print(f"{a} is your OTP. Do not share with anyone.")

# Calling the function
otp()