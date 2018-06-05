
def solution(A):

    if(not A):
        return 0
    n=len(A)

    if(n==0):
        return 0


    lowdiff = -1
    n=len(A)
    for i in range(1,n):
        part1 = getSum(A,0,i)
        part2=getSum(A,i,n)

        print part1
        print part2

        if (lowdiff == -1):
            lowdiff = abs(part1-part2)
        else:
            lowdiff = min(lowdiff,(abs(part1-part2)))

    return lowdiff

def getSum(A,start,end):

    total=0
    for i in range(start,end):
        total+=A[i]

    return total

#best solution
def solution(A):
    right = A[0]
    left = sum(A[1:])
    dif = abs(right - left)

    for index in range(1, len(A)-1):
        right += A[index]
        left -= A[index]

        dif=min(dif,abs(right - left))


    return dif
A = [ 3, 1, 2, 4,3]
print A
#print(solution(A))
print solution(A)
