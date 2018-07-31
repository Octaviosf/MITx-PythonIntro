balance = 320000
annualInterestRate = 0.2
#variable initialization
monthlyInterestRate = annualInterestRate/12
newBalance = balance
low = round(newBalance / 12,2)
high = round(newBalance*(1+monthlyInterestRate)**12/12,2)
minFixedPayment = round(low + (high-low)/2,2)
#Loop to calculate payment of loan in 1 year or less
while newBalance > 0.25 or newBalance < -0.25:
    newBalance = balance
    #calculates balance after 1 year using an iterated minimum fixed payment
    for i in range(12):
        monthlyUnpaidBalance = newBalance - minFixedPayment
        newBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance

    newBalance = round(newBalance,2)
    print('balance:',newBalance)
    print('low:',low)
    print('payment:',minFixedPayment)
    print('high:',high)
    #if balance is 0 after 1 year then print minimum fixed payment
    if newBalance < 0.25 and newBalance > -0.25:
        print('Lowest Payment:', minFixedPayment)
        break
    #if balance remains after mininum fixed payment of 1 year create new fixed payment
    elif newBalance > 0.25:
        low = minFixedPayment
        minFixedPayment = round(low + (high-low)/2,2)
    elif newBalance < -0.25:
        high = minFixedPayment
        minFixedPayment = round(low + (high-low)/2,2)