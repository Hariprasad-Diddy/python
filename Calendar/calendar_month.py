# importing module
import calendar

# taking input from the user 
c_year = input("Enter which year caledar : ")
c_month = input("Enter particular month in that year or press Q to print entire year: ")

# checking user wants to print entire year 
if c_month == "" or c_month == 'Q' or c_month == 'q':
    print(calendar.calendar(int(c_year)))
    
# checking user wants to print particular month
else:
    print(calendar.month(int(c_year),int(c_month)))