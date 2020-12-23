from math import log
from math import ceil
import argparse
import sys

if len(sys.argv) == 5:
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', required=True, choices=['annuity', 'diff'])
    parser.add_argument('--principal', type=int)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=int)
    parser.add_argument('--periods', type=int)
    args = parser.parse_args()
    if args.type == 'annuity':
        if args.payment is None:
            principal = args.principal
            periods = args.periods
            interest = args.interest
            i = interest / (12 * 100)
            power = pow(1 + i, periods)
            numerator = i * power
            denominator = power - 1
            annuity_payment_raw = principal * numerator / denominator
            annuity_payment_last = ceil(annuity_payment_raw)
            sum_of_payments = annuity_payment_last * periods
            overpayment = sum_of_payments - principal
            print("Your annuity payment = " + str(annuity_payment_last) + "!")
            print("Overpayment = " + str(overpayment))
        elif args.principal is None:
            payment = args.payment
            periods = args.periods
            interest = args.interest
            i = interest / (12 * 100)
            power = pow(1 + i, periods)
            numerator_of_denominator = i * power
            denominator_of_denominator = power - 1
            fraction = numerator_of_denominator / denominator_of_denominator
            principal_raw = payment / fraction
            principal_last = ceil(principal_raw)
            sum_of_payments = payment * periods
            overpayment = sum_of_payments - principal_last
            print("Your credit principal = " + str(principal_last) + "!")
            print("Overpayment = " + str(overpayment))
        elif args.periods is None:
            principal = args.principal
            payment = args.payment
            interest = args.interest
            i = interest / (12 * 100)
            base = i + 1
            denominator = payment - i * principal
            middle = payment / denominator
            n = log(middle, base)
            rounded = ceil(n)
            sum_of_payments = payment * rounded
            overpayment = sum_of_payments - principal
            if rounded >= 12:
                years = rounded // 12;
                difference = rounded - (years * 12)
                if difference == 0:
                    print("You need " + str(years) + " years to repay this credit!")
                else:
                    print("You need " + str(years) + " years and " + str(difference) + " months to repay this credit!")
            else:
                print("You need " + str(rounded) + " months to repay this credit!")
            print("Overpayment = " + str(overpayment))

    else:
        periods = args.periods
        principal = args.principal
        interest = args.interest
        if interest is None:
            print("Incorrect parameters")
        else:
            i = interest / (12 * 100)
            counter = 1
            sum_of_payments = 0
            while counter <= periods:
                first_section = principal / periods
                second_section = i * (principal - (principal * (counter - 1)) / periods)
                total_payment = first_section + second_section
                rounded = ceil(total_payment)
                sum_of_payments += rounded
                print("Month " + str(counter) + ": paid out " + str(rounded))
                counter += 1
            overpayment = sum_of_payments - principal
            print()
            print("Overpayment = " + str(overpayment))
else:
    print("Incorrect parameters")