### Part A (Determine how long it will take you to save enough money to make
# the down payment)

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary / 12

month = 0
while (portion_down_payment > current_savings):
    investment_interest_per_month = current_savings * (0.04/12);
    current_savings += investment_interest_per_month + (monthly_salary * portion_saved)
    month += 1

print("Number of months:", month)