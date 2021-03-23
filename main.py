
class value ():
    RED = '\033[31m'

print(value.RED )

P=int(input('How much would you like to invest:'))
a=float(input('What is the rate of intrest on your account:'))
t=int(input('How long are you planning to invest:'))
n=int(input('What is the number of times the intrest is compound per year:'))
r=a/100
g=n*t
A=P*(1+r/n)**g
L=P*(r/4)
N=(P+1)
D=n*t
formated_l=format(P*(r/4),'.2f')
formated_N=format((P+1),'2f')
formated_A=format(A,'.2f')
print('Rs',P ,',a,%for',t,'years compounded ',n,'times per year is:RS',formated_A)