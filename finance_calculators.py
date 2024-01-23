import math

# This is an interest and loan repayment calculator.

# Ask the user to choose between investment or loan repayment.
option = input("""investment - to calculate the amount of interest you'll earn on your investment 
bond \t   - to calculate the amount you'll have to pay on a home loan\n
Enter either 'investment' or 'bond' from the menu above to proceed: """)

# If the user has chosen investment, they will now be asked to imput a few essential details.
# Using an if, elif, else statement, the details will be processed and calculated as float numbers, and will display the total amount
# accummulated with their interest.
# The user will also be asked to choose between simple and compound, as these types of interest will be calculated differently.
if option.lower() == "investment":
    original_amount = float(input("\nPlease enter the amount that you would like to deposit here: "))
    interest_rate = float(input("\nPlease enter the interest rate here( enter numbers without the '%'): "))
    years_of_investment = float(input("\nPlease enter the number of years that you are planning to invest for: "))
    interest = input("""\nPlease specify the type of interest you will be earning:\
                     \n\nsimple      - calculated yearly based on the amount initially invested\
                     \ncompound    - calculated based on the total accumulated each year\
                     \n\nEnter either 'simple' or 'compound' from the menu above to calculate your interest: """)
    simple_earnings = original_amount * (1 + (interest_rate / 100) * years_of_investment)
    compound_earnings = original_amount * math.pow((1 + interest_rate / 100), years_of_investment)
    if interest.lower() == "simple":
        print("\nThe amount invested will increase to £" + str(simple_earnings) + ", based on the details provided.")
    elif interest.lower() == "compound":
        print("\nThe amount invested will increase to £" + str(compound_earnings) + ", based on the details provided.")
    else:
        print("Please choose a valid option.")     
# The second option will calculate the amount of money the user would have to pay per month, in order to repay a home loan.
# The monthly repayment interest will be taken into account.
elif option.lower() == "bond":
    value = float(input("\nPlease enter the current value of the house here: "))
    interest_rate_loan = float(input("\nPlease enter the interest rate here( enter numbers without the '%'): "))
    months_of_repayment = float(input("\nPlease specify how many months you are planning to take to repay the bond here: "))
    monthly_interest = (interest_rate_loan / 100) / 12
    monthly_repayment = (monthly_interest * value) / (1 - (1 + monthly_interest) ** (- months_of_repayment))
    print(f"\nTo repay this loan over {months_of_repayment} months, you would have to pay £{monthly_repayment} each month.")
# If the user types something else, not investment or bond, the program will respond by asking the user to select one of the two available options.
else:
    print("\nError! Please choose one of the two services mentioned above!")
