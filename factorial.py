def factorial(n):
    if n<0:
        return"fatorial is cannot be negative number"
    elif n==0:
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result *=i
        return result
num=int(input())
n=factorial(num)
print(n)
