def miniValue(A,B,n):
    A.sort()
    B.sort()
    result = 0
    for i in range(n):
        result += (A[i] * B[n - i - 1])

    return result

A = [3,1,1]
B = [6,5,4]
n = len(A)
print(miniValue(A,B,n))