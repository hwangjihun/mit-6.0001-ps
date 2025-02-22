### Part C Bruteforce (slightly more efficient bruteforce)
starting_salary = float(input("Enter the starting salary: "))
semi_annual_raise = 0.07
portion_down_payment = 0.25 * 1000000
found = False

for i in range (10000):
    current_savings_rate = i / 10000
    current_savings = 0
    months_taken = 0
    monthly_salary = starting_salary / 12
    for months_taken in range(1, 37):
        investment_interest_per_month = current_savings * (0.04/12)
        current_savings += investment_interest_per_month + (monthly_salary * current_savings_rate)
        if (months_taken % 6 == 0):
            monthly_salary *= (1 + semi_annual_raise)
    if (current_savings >= portion_down_payment - 100 and current_savings <= portion_down_payment + 100):
        print("Best savings rate:", current_savings_rate)
        found = True
        break        

if (found == False):
    print("It is not possible to pay the down payment in three years.")