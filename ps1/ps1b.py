### Part B

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary / 12

month = 0
while (portion_down_payment > current_savings):
    investment_interest_per_month = current_savings * (0.04/12);
    current_savings += investment_interest_per_month + (monthly_salary * portion_saved)
    month += 1
    if (month % 6 == 0):
        monthly_salary *= (1 + semi_annual_raise)
print("Number of months:", month)