year = int(input("Enter Year : "))

def leap_year(year):
    """
	Year which is divisable by 4 and 
	divisible by 100 and not equal to 0 or 
	divisable by 400 was a Leap Year
	"""
    if ((year % 4 ==0) and (year % 100 !=0) or (year % 400 == 0)):
        print("%d is a Leap Year!!" % year)
    else:
        print("%d is not a Leap year!!" % year)
leap_year(year)