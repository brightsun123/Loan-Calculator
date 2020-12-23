from math import log
from math import ceil

print("What do you want to calculate?")
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
action = input()

if action == "n":
    print("Enter credit principal:")
    principal = int(input())
    print("Enter monthly payment:")
    payment = float(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    base = i + 1
    denominator = payment - i * principal
    middle = payment / denominator
    n = log(middle, base)
    rounded = ceil(n)
    if rounded >= 12:
        years = rounded // 12;
        difference = rounded - (years * 12)
        if difference == 0:
            print("You need " + str(years) + " years to repay this credit!")
        else:
            print("You need " + str(years) + " years and " + str(difference) + " months to repay this credit!")
    else:
        print("You need " + str(rounded) + " months to repay this credit!")

elif action == "a":
    print("Enter credit principal:")
    principal = int(input())
    print("Enter count of periods:")
    periods = int(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    power = pow(1 + i, periods)
    numerator = i * power
    denominator = power - 1
    annuity_payment_raw = principal * numerator / denominator
    annuity_payment_last = ceil(annuity_payment_raw)
    print("Your annuity payment = " + str(annuity_payment_last) + "!")

elif action == "p":
    print("Enter monthly payment:")
    payment = float(input())
    print("Enter count of periods:")
    periods = int(input())
    print("Enter credit interest:")
    interest = float(input())
    i = interest / (12 * 100)
    power = pow(1 + i, periods)
    numerator_of_denominator = i * power
    denominator_of_denominator = power - 1
    fraction = numerator_of_denominator / denominator_of_denominator
    principal_raw = payment / fraction
    principal_last = ceil(principal_raw)
    print("Your credit principal = " + str(principal_last) + "!")

