monthlyInterestRate = annualInterestRate/12
l = 0
h = (balance * (1+monthlyInterestRate)**12) / 12
if annualInterestRate == 0:
    print('Lowest Payment: ' + str(round(balance/12,2)))
while True:
    tempBalance = balance
    fixPay = ((l + h) / 2)
    for i in range(1,13):
        monthlyUnpaidBlance = tempBalance - fixPay
        tempBalance = monthlyUnpaidBlance + (monthlyInterestRate * monthlyUnpaidBlance)

    if abs(tempBalance) < 0.01:
        print('Lowest Payment: ' + str(round(fixPay,2)))
        break
    elif tempBalance > 0:
        l = fixPay
    elif tempBalance < 0:
        h = fixPay  