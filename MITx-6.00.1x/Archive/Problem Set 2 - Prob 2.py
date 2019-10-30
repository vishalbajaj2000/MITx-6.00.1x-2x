##-----------Problem 2------------
balance = 330
annualInterestRate = 0.2
# the able 2 fields are not for edx
balancex = balance
monthlyInterestRate = annualInterestRate / 12
step = 10
monthlyPayment = int(round(balance / 12, -1))
if annualInterestRate == 0:
    print('Lowest Payment:',balance)
else:
    while balancex != 0:
        balancex = balance
        i = 1
        unpaid = 0
        for i in range (1,12):
            balancex = balancex - monthlyPayment
            unpaid = balancex + (balancex * monthlyInterestRate)
            balancex = unpaid
            i += 1
        if balancex <= monthlyPayment:
            print('Lowest Payment:',int(monthlyPayment))
            break
        if round(balancex,-1) > 10:
            monthlyPayment += step
