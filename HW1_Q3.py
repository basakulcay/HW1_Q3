# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:15:29 2020

@author: PC
"""

# Q3: In this question we tried to develop a calculation tool for a bank.
# Initially we take a response from our customer about whether he/she wants 
# to open deposit account or to get a credit.

# In case our customer press d, yearly deposit rate appears at the screen and then we
# get the investment amount and investment interval information. By using this
# information we calculate the interest and total investmnet.

# In case our customer press c, monthly credit rate appears at the screen and then we
# get the amount and maturity information of credit. By using this information 
# we calculate monthly installment amounts.

# In case our customer press different letter our program will ask until it takes d or c

print ("\n***Welcome Bis511BANK***")
print ('How can we help you? Do you want to deposit your money, or want to get credit?')
response= str(input ("Please press 'd' to learn deposit rates and press 'c' to learn credit rates:"))

deposit=18 

credit=1.79

while (response!='d') and (response!='c'):
    response= str(input ("Please press 'd' to learn deposit rates and press 'c' to learn credit rates:"))


if (response=='d'):
    print ("\nYearly Deposit Rate is equal to %", deposit)
    amount=float(input("How much money do you want to invest: "))
    interval=int(input("How many years do you want to invest: "))
    print('\n*****Your Return Plan Is Below***** \n\nYear\t Currency\tInterest\t\tTotal Amount')
    print('------------------------------------------')
    for i in range(interval):
        i=i+1
        interest=amount*0.18
        amount=amount*1.18
        print (i, 'TL', format (interest, ',.2f'), format(amount, ',.2f'), sep='\t\t')
        
elif (response=='c'):
    print ("Monthly Credit Rate is equal to %", credit)
    amount=float(input("How much money do you want to take as credit: "))
    tt=amount
    interval=int(input("In how many months will you pay back: "))
    print('\n*****Your Payment Plan Is Below***** \n\nMonth\tCurrency\t\tInterest\t\tPrincipal\t\tInstallment Amount')
    print('-------------------------------------------------------------------')
    for i in range(interval):
        i=i+1
        interest=tt*0.0179
        principal=(amount/interval)
        tt=tt-principal
        total=interest+principal
        print (i, 'TL', format (interest, ',.2f'), format(principal, ',.2f'), format(total, ',.2f'),sep='         ')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
