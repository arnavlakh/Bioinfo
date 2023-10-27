a = int(input("enter value of first integer: "))
b = int(input("enter value of second integer: "))
#sum = a
x=a
#for b>x:
#if a%2==1 & b%2==1:
#        x = a+2
#        sum= sum+x
#        a= a+2  
#elif a%2==1 & b%2==0:
#        x = a+2
#        sum=x+sum
#        a= a+2
#elif a%2==0 & b%2==1:
#        a=a+1
#        sum=a
#   

y = []
for i in range(a,b+1):
    y.append(i)
    for j in range(len(y)):
        if y[j]%2==0:
            y.pop(j)


print(sum(y))

