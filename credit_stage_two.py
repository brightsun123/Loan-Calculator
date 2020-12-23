print("Enter the credit principal: ")
principal = int(input())
print("What do you want to calculate?")
print('type "m" - for count of months,')
print('type "p" - for monthly payment:')
action = input()
if action == "m":
    print("Enter monthly payment")
    payment = int(input())
    print("")
    months = (principal + payment - 1) // payment
    print("")
    if months > 1:
        print("It takes " + str(months) + " months to repay the credit")
    else:
        print("It takes 1 month to repay the credit")
else:
    print("Enter count of months:")
    months = int(input())
    print("")
    monthly_payment = (principal + months - 1) // months
    if monthly_payment * months == principal:
        print("Your monthly payment = " + str(monthly_payment))
    else:
        value = months - 1
        last_payment = principal - value * monthly_payment
        print("Your monthly payment = " + str(monthly_payment) + " with last month payment = " + str(last_payment) + ".")
