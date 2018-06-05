# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):


    N=len(A)
    if(not A):
        return A

    while(K > N):
        K = K-N

    if(N <= 0 or N==1 or K <=0 or N>100 and K>100):
        return A
    if max(list(A)) > 1000:
        return A

    if min(list(A)) < -1000:
        return A
    newi=-1
    Arotated = [0] * N
    for i in range(N):
        newi = i+K
        if(newi >= N):
            newi= newi-N
        Arotated[newi] = A[i]

    return Arotated
