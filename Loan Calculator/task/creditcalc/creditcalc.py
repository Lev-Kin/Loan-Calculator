import math

def calculate_monthly_payments(principal, payment, interest):
    interest = interest / 100 / 12
    months = math.log(payment / (payment - interest * principal), 1 + interest)
    return math.ceil(months)

def calculate_monthly_payment(principal, periods, interest):
    interest = interest / 100 / 12
    payment = principal * (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)
    return math.ceil(payment)

def calculate_loan_principal(payment, periods, interest):
    interest = interest / 100 / 12
    principal = payment / ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1))
    return principal

calculation_type = input("What do you want to calculate?\n"
                         'type "n" for number of monthly payments,\n'
                         'type "a" for annuity monthly payment amount,\n'
                         'type "p" for loan principal:\n')

if calculation_type == 'n':
    principal = float(input("Enter the loan principal:\n"))
    payment = float(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    months = calculate_monthly_payments(principal, payment, interest)
    years, months = divmod(months, 12)
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

elif calculation_type == 'a':
    principal = float(input("Enter the loan principal:\n"))
    periods = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    payment = calculate_monthly_payment(principal, periods, interest)
    print(f"Your monthly payment = {payment}!")

elif calculation_type == 'p':
    payment = float(input("Enter the annuity payment:\n"))
    periods = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    principal = calculate_loan_principal(payment, periods, interest)
    print(f"Your loan principal = {principal}!")
