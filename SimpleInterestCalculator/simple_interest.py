def simple_interest():
    # Principal Amount
    p = float(input("Enter Loan Amount : "))
    # Rate of Interest Anually
    r = float(input("Enter Rate Of Interest : "))
    # Tenure
    t = float(input("Enter Tenure in Years : "))
    # Calculating the Interest
    final_interest = p * r * t
    print("Thanks for waiting, Interest calculated after {} years the interest you have to pay is {:.2f}".format(round(t),final_interest))  

simple_interest()