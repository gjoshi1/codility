def solution(A, N):
    result = 0
    for number in A:
        result ^= number

    return result


def printloop(A,N):
    for i in xrange(N):
        print "  "
        print A[i]
        print "  "
        for j in xrange(i+1,N):
            if(A[i] == A[j]):
                print A[j]
A = [9 ,3 , 9, 3, 9, 7, 9]
print(solution(A,7))
#printloop(A,7)
