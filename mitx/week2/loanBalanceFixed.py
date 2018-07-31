#variable initialization
monthlyInterestRate = annualInterestRate/12
minFixedPayment = 10
newBalance = balance
#Loop to calculate payment of loan in 1 year or less
while newBalance > 0:
    newBalance = balance
    #calculates balance after 1 year using an iterated minimum fixed payment
    for i in range(12):
        monthlyUnpaidBalance = newBalance - minFixedPayment
        newBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance

    #if balance is 0 or less after 1 year then print minimum fixed payment
    if newBalance <= 0:
        print('Lowest Payment:', minFixedPayment)
        break
    #if balance remains after mininum fixed payment of 1 year increment fixed payment by $10
    else:
        minFixedPayment += 10
