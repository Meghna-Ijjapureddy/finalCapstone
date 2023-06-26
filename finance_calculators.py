import math

print("investment - to calculate the amount of interest you'll earn on your investment") # Displaying investment calculator
print("bond - to calculate the amount you'll have to pay on a home loan") # Displaying bond calculator

# Asking user to choose the type of calculation user wants to perform
CalculationType = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # converting the input to lower case

if CalculationType != "investment" and CalculationType != "bond":
    print("Invalid entry. Please choose from the list mentioned")

else: # Asking the user to enter details when investment calculator is selected
    if CalculationType == "investment":
        Deposit = float(input("Please enter the amount that you are depositing: "))
        InterestRate_investment = float(input("Please enter the interest rate: ").strip("%"))
        number_of_years = float(input("Please enter the number of years you are planning to invest for: "))
        Interest = input("Please enter if you would want simple or compound interet. Enter 'simple' for simple interest and 'compound' for compound interest: ").lower()
    # Total amount calculation when user enters simple interest
        if Interest == "simple":
            total_amount = Deposit*(1+(InterestRate_investment/100)*number_of_years)
            print("Total amount you will get back after given period is ", total_amount)
    # Total amount calculation when user enters compound interest
        if Interest == "compound":
            total_amount = Deposit*math.pow((1+(InterestRate_investment/100)),number_of_years)
            print("Total amount you will get back after given period is ", total_amount)
# Asking the user to enter details when bond calculator is selected
    if CalculationType == "bond":
        Current_Value_of_house = float(input("Please enter the current value of the house: "))
        InterestRate_bond = float(input("Please enter the interest rate: ").strip("%"))
        number_of_months = float(input("Please enter the number of months you are planning to repay the bond in: "))
        Repayment = ((InterestRate_bond/1200)*Current_Value_of_house)/(1-(1+(InterestRate_bond/1200))**(-number_of_months))
        print ("The money you will need to pay every month is equal to", Repayment)