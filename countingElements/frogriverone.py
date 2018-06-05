
def solution(X,A):
    if(X <=0 or not A or len(A) == 0 ):
        return -1
    covered = 0
    n=len(A)
    L = [0] * X



    time=-1

    for t in range(n):

        if(A[t]<0 or A[t]>X):
            raise Exception("Invalid value", A[t])
        if(L[A[t]-1] == 0):
            L[A[t]-1] = 1
            covered+=1
            if(covered == X):
                time=t
                break





    return time











A=[1,3,1,4,2,3,5,4]
X=5
print(solution(X,A))
