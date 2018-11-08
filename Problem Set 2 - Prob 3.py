##-----------Problem 3------------
balance = 320000
annualInterestRate = 0.2
# the able 2 fields are not for edx

monthlyInterestRate = annualInterestRate / 12
balancex = balance
lowerB = balance / 12
upperB = (balance * (1 + monthlyInterestRate)**12) / 12.0


if annualInterestRate == 0:
    print('Lowest Payment:',balance)
else:
    while balancex != 0.00:
        monthlyPayment = round((lowerB + upperB) / 2, 2)
        balancex = balance
        i = 1
        unpaid = 0
        for i in range (1,13):
            balancex = balancex - monthlyPayment
            unpaid = balancex + (balancex * monthlyInterestRate)
            balancex = unpaid
            i += 1
        if int(balancex) == 0:
            print('Lowest Payment:',monthlyPayment)
            break
        if balancex > 0:
            lowerB = (upperB + lowerB) / 2
            print('too low:',monthlyPayment, 'balance is', round(balancex,2), 'ub', upperB, 'lb', lowerB )
        if balancex < 0:
            upperB = (upperB + lowerB) / 2
            print('too high:',monthlyPayment, 'balance is', round(balancex,2), 'ub', upperB, 'lb', lowerB )