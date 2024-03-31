import math

# Print the two types of calculation
print("investment - the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Prompt for the user to choose a calculation from the options above
calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Calculations
while True:

    # Bond Calculation
    if calculation == "bond":
        print("Calculating the bond..")

        # Get input for bond calculation
        present_value = float(input("Enter the present value of the house (in USD): "))
        interest_rate_bond = float(input("Enter the annual interest rate (as a percentage): "))
        months = int(input("Enter the number of months to repay the bond: "))

        # Convert annual interest rate to monthly interest rate
        i = (interest_rate_bond / 100) / 12

        # Calculate the monthly bond repayment
        repayment = (i * present_value) / (1 - math.pow((1 + i), -months))

        print(f"Your monthly bond repayment will be ${repayment:.2f} for {months} months.")
        break

    # Investment calculation
    elif calculation == "investment":
        print("Calculating the investment..")

        # Get input for investment calculation
        deposit_amount = float(input("Enter the amount of money you are depositing (in USD): "))
        interest_rate = float(input("Enter the interest rate (as a percentage): "))
        t = int(input("Enter the number of years you plan on investing: "))
        interest = input("Enter 'simple' or 'compound' interest: ").lower()

        # Convert interest rate to decimal
        r = interest_rate / 100

        # Calculate the future value based on the interest type
        while True:
            # Future value if interest is simple
            if interest == "simple":
                future_value = deposit_amount * (1 + r * t)
                break
            # Future value if interest is compound
            elif interest == "compound":
                future_value = deposit_amount * math.pow((1 + r), t)
                break
            # Prompt user again if invalid interest type entered
            else:
                print("Invalid interest type. Please enter 'simple' or 'compound'.")
                interest = input("Enter 'simple' or 'compound' interest: ").lower()

        print(f"Your investment will be worth ${future_value:.2f} after {t} years.")
        break
    
    # If not valid option prompt again until valid option is entered by the user
    else:
        print("Please enter a valid calculation from the menu")
        calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()