#CONVERTING time
seconds=int(input ("Please Enter Seconds"))
hours=seconds//3600
minutes=seconds%3600//60
sec=seconds%3600%60
print ("Seconds =",sec)
print ("Minutes =", minutes)
print ("Hours =", hours)

#Savings Account

P=int(input("Please Enter Deposit Amount"))
F=int(input("Please Enter Future Value Desired"))
r=float(input("Please Enter Interest Rate"))
n=int(input("Please Enter Number of Years"))
money=F/(1+r)**n
print (money)
