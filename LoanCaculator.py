Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # enter
>>> # enter annual interest rate as 1.05
>>> annualInterestRate = eval(input("Plz Enter Annual Interest Rate as:  "))
Plz Enter Annual Interest Rate as:  
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    annualInterestRate = eval(input("Plz Enter Annual Interest Rate as:  "))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> annualInterestRate = eval(input("Plz Enter Annual Interest Rate as:  "))
Plz Enter Annual Interest Rate as:  1.05
>>> monthlyInterestRate = annualInterestRate / 12
>>> # enter number of years
>>> numOfYears = eval(input("Plz Enter Number of Years:  "))
Plz Enter Number of Years:  20
>>> # enter loan amount
>>> loanAmount = eval(input("Plz Enter Loan Amount in dollars: "))
Plz Enter Loan Amount in dollars: 30,000
>>> # calculate payment which is set monthly
>>> monthlyPayment = loanAmount * monthlyInterestRate
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    monthlyPayment = loanAmount * monthlyInterestRate
TypeError: can't multiply sequence by non-int of type 'float'
>>> totalPay = monthlyPayment * 12 * numOfYears
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    totalPay = monthlyPayment * 12 * numOfYears
NameError: name 'monthlyPayment' is not defined
>>> annualInterestRate = eval(input("Plz Enter Annual Interest Rate as:  "))
Plz Enter Annual Interest Rate as:  7.25
>>> monthlyInterestRate = annualInterestRate / 12
>>> monthlyPayment = loanAmount * monthlyInterestRate
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    monthlyPayment = loanAmount * monthlyInterestRate
TypeError: can't multiply sequence by non-int of type 'float'
>>> monthlyPayment = loanAmount * int(monthlyInterestRate)
>>> totalPayment = monthlyPayment * 12 * numOfYears
>>> 
>>> print(totalPayment)
()
>>> print("Total Payment is:" totalPayment)
SyntaxError: invalid syntax
>>> print("Total Payment is:", totalPayment)
Total Payment is: ()
>>> print("Monthly Payment is:", monthlyPayment)
Monthly Payment is: ()
>>> 