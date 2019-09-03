##------------Problem 1-----------
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# the able 3 fields are not for edx

monthlyInterestRate = annualInterestRate / 12
x = 1

while x <= 12:
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    x += 1
print(round(balance,2))