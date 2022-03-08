def simple_interest():
    # Principal Amount
    principal = float(input("Enter Loan Amount : "))
    # Rate of Interest Anually
    rate_of_interest = float(input("Enter Rate Of Interest : "))
    # Tenure
    period = input("Enter Year or Month the you repay the Loan : ")
    # Calculating the Interest

    if period.capitalize() == "Year":
       tenure = int(input("Enter No.of Years : "))
    elif period.capitalize() == "Month":
       tenure = int(input("Enter No.of Months : "))
       tenure = tenure/12
    rate_of_interest = rate_of_interest/100
    final_interest = principal * (1+(rate_of_interest * tenure))
    print("Thanks for waiting, Interest calculated after {} years the interest you have to pay is {:.2f}".format(round(tenure),final_interest))  

simple_interest()