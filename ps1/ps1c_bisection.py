### Part C Bisection Search (similar to binary search)
starting_salary = float(input("Enter the starting salary: "))
semi_annual_raise = 0.07
portion_down_payment = 0.25 * 1000000
max_savings_rate = 10000
low_rate = 0
high_rate = max_savings_rate
current_savings_rate = (low_rate + high_rate) / 2.0
epsilon = 100
current_savings = 0
steps = 0 
impossible = False

while (abs(current_savings - portion_down_payment) >= epsilon):
    # even with a savings rate of 99%, the code is still reiterating which means it is impossible to find a soln
    if (current_savings_rate / 10000 >= 0.99):
        print("It is not possible to pay the down payment in three years.")
        impossible = True
        break
    monthly_salary = starting_salary / 12
    current_savings = 0
    for months_taken in range(1, 37):
        investment_interest_per_month = current_savings * (0.04 / 12)
        current_savings += investment_interest_per_month + (monthly_salary * (current_savings_rate / 10000))
        if (months_taken % 6 == 0):
            monthly_salary *= (1 + semi_annual_raise)
    if (current_savings < portion_down_payment):
        low_rate = current_savings_rate
    else:
        high_rate = current_savings_rate
    current_savings_rate = (low_rate + high_rate) / 2.0
    steps += 1

if (not impossible):
    print("Best savings rate:", current_savings_rate / 10000)
    print("Steps in bisection search:", steps)