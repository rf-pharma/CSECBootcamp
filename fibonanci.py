def fibo(n):
    seq=[]
    a,b=0,1
    while len(seq) <n:
        seq.append(a)
        a,b=b,a+b
    return seq
num=int(input())
fibb=fibo(num)
print(fibb)