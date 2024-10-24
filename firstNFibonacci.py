def fib(n):
    fib_seq = []
    a = 0
    b = 1

    for i in range(n):
        fib_seq.append(a)
        temp = a  
        a = b
        b = temp + b

        # a,b = b, a+b

    return fib_seq


print(fib(10))