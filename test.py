def solution(A):

    n=len(A)
    ctr=[0] * n
    if n ==0:
        return 0

    count=1
    #head
    node=A[0]

    #traverse until tail value -1 os reached
    while(node != -1):
        node = A[node]
        ctr[A[node]] +=1
        if(ctr[A[node]] > 1):
            return 0
        #the node value cannot be > size of array and < -1
        if(node > n-1 or node < -1):
            return 0
        count+=1

    return count
A=[1, 4, -1, 3, 4]

print(solution(A))
