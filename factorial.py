def factorial(n):
    if n<=0:
        return 0
    result=1
    while n>1:
        result*=n
        n=n-1
    return result
