from curses.ascii import isalpha


def arm_strong(num):
    
    check = [(int(l) ** len(num)) for l in num]
    print(f"{num} was a ARM Strong number ....!") if sum(check) == int(num) else print(f"{num} was not a ARM Strong number.")

num = input("Enter number to check : ") 
arm_strong(num)

