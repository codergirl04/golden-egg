def fib(num):
    fib1 = 1
    fib2 = 1
    ans = 0
    sub = 0
    while ans <= num:
        if ans == num:
            return ans
        temp = 0
        temp = fib1
        fib1 = fib2
        fib2 = temp+fib2
        ans = fib1+fib2
        sub = ans - fib2
    return ans-sub

print(fib(98))