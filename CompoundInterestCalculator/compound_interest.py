def compound_interest():
    # Principal Amount
    p = float(input("Enter Principal Amount : "))
    # Rate of Interest
    r = float(input("Enter Rate of Interest : "))
    # Tenure
    t = int(input("Enter Tenure Years : "))
    
    # Calculating Compound Interest
    total_interest = 0
    total_amount = p
    for i in range(0,t):
        b = (r*total_amount/100)
        total_amount +=b
        total_interest += b
    print("Thanks for waiting, Interest Calculated for {}, you have to pay Rs {:.2f}/- of Amount as Interest after {} years \nTotal {}".format(p,total_interest,t,total_amount))

compound_interest()