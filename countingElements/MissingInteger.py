def solution(A):

    missingNum=-1

    if(not A):
        return 1

    n=len(A)
    if(n==0):
        return -1

    c = [0] * (n+1)

    for i in range(n):
        if(A[i] >=1 and A[i] <= n+1):
            c[A[i]-1] = 1

    for j in range(len(c)+1):
        if c[j] == 0:
            missingNum=j+1
            break

    return missingNum
