def diff(f,m):
    if m==1:
        return((f(a+10**(-12),b)-f(a,b))/10**(-12))
    if m==2:
        return((f(a,b+10**(-12))-f(a,b))/10**(-12))
    
x=[i+50 for i in range(0,10)]
y=[496,515,503,529,553,546,564,566,582,587]
def error(a,b):
    return(sum((a*x[i]+b-y[i])**2 for i in range(0,10)))
a=0
b=0
e1=0
e2=99999
i=0
while abs(e2-e1)>10**(-10) and (abs(diff(error,1))>.1 or abs(diff(error,2))>.1):
    if abs(e2-e1)>10**5:
        A1=10**(-5)
        A2=10**(-5)
        e1=error(a,b)
        tempa=a-A1*diff(error,1)
        tempb=b-A2*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(abs(e2-e1))
        i=i+1
    elif 10**5>abs(e2-e1)>=100:
        A1=10**(-6)
        A2=10**(-6)
        e1=error(a,b)
        tempa=a-A1*diff(error,1)
        tempb=b-A2*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(abs(e2-e1))
        i=i+1
    elif .01<=abs(e2-e1)<100:
        A1=10**(-7)
        A2=10**(-7)
        e1=error(a,b)
        tempa=a-A1*diff(error,1)
        tempb=b-A2*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(abs(e2-e1))
        i=i+1
    elif abs(e2-e1)<.01:
        A1=10**(-8)
        A2=10**(-8)
        e1=error(a,b)
        tempa=a-A1*diff(error,1)
        tempb=b-A2*diff(error,2)
        a=tempa
        b=tempb
        e2=error(a,b)
        print(abs(e2-e1))
        i=i+1
print()
print(f'the value of a,b are:')
print(a,b)
print(f'The minimized error is:')
print(error(a,b))
print(f'Now abs(e2-e1) is:')
print(abs(e2-e1))
