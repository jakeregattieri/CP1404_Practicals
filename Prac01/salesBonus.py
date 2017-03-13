"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter Sales: $"))
while sales > 0:
    if sales < 1000:
        bonus = sales * 10/100
    else:
        bonus = sales * 15/100
    print("Your total bonus: $" + str(bonus))
    sales = float(input("Enter Sales: $"))

