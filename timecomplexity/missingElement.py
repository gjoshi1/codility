def solution(A):

    if(not A):
        return -1

    n=len(A)

    if(n==0):
        return -1

    n=n+1
    totalSum = n*(n+1) //2

    sumOfArrValues=0
    missingNum = -1

    for val in A :
        sumOfArrValues += val

    missingNum = totalSum-sumOfArrValues
    return missingNum

A = [ 1, 3, 2, 5,4,6]

print(solution(A))
