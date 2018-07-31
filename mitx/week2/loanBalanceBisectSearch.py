#variable initialization
monthlyInterestRate = annualInterestRate/12
newBalance = balance
low = round(newBalance / 12,2)
high = round(newBalance*(1+monthlyInterestRate)**12/12,2)
minFixedPayment = round(low + (high-low)/2,2)
#Loop to calculate payment of loan in 1 year or less
while newBalance != 0.00 :
    newBalance = balance
    #calculates balance after 1 year using an iterated minimum fixed payment
    for i in range(12):
        monthlyUnpaidBalance = newBalance - minFixedPayment
        newBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance

    round(newBalance,2)
    #if balance is 0 after 1 year then print minimum fixed payment
    if newBalance == 0.00:
        print('Lowest Payment:', minFixedPayment)
        break
    #if balance remains after mininum fixed payment of 1 year create new fixed payment
    elif newBalance > 0:
        low = minFixedPayment
        minFixedPayment = round(low + (high-low)/2,2)
    elif newBalance < 0:
        high = minFixedPayment
        minFixedPayment = round(low + (high-low)/2,2)
