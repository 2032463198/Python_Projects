import math
def diff(f,m):
    if m==1:
        return((f(a+10**(-12),b)-f(a,b))/10**(-12))
    if m==2:
        return((f(a,b+10**(-12))-f(a,b))/10**(-12))
    
x=[i+30 for i in range(0,10)]
y=[0.93,0.9,0.95,0.98,0.97,0.04,0.06,0.05,0.1,0.08]
def error(a,b):
    return(sum(-y[i]*math.log(1/(1+10**(a*x[i]+b)))-(1-y[i])*math.log(1-1/(1+10**(a*x[i]+b))) for i in range(0,10)))
a=b=1
e1=0
e2=1
while abs(e2-e1)>10**(-7) or ((abs(diff(error,1))>.1 or abs(diff(error,2))>.1)):
    if abs(e2-e1)>=.01:
        A=0.0015
        e1=error(a,b)
        tempa=a-A*diff(error,1)
        tempb=b-A*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(a,b)
        #print(abs(e2-e1))
    elif .01>abs(e2-e1)>=10**(-4):
        A=10**(-4)
        e1=error(a,b)
        tempa=a-A*diff(error,1)
        tempb=b-A*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(abs(e2-e1))
    else:
        A=10**(-5)
        e1=error(a,b)
        tempa=a-A*diff(error,1)
        tempb=b-A*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(abs(e2-e1))
print()
print(f'the value of a,b are:')
print(a,b)
print(f'The minimized error is:')
print(error(a,b))
print(f'Now abs(e2-e1) is:')
print(abs(e2-e1))
