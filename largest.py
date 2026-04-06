def large(n):
    if not n:
        return"empty"
    return max(n)
num=list(map(int,input().split()))
larger=large(num)
print(larger)