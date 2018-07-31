
monthlyInterest = annualInterestRate/12

for i in range(12):
    minMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterest*monthlyUnpaidBalance

print('Remaining balance:',round(balance,2))