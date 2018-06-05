# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    if(X<=0 or Y<=0 or D<=0 or Y<=X or D > Y):
        return 0

    tistancetocover = (Y-X)

    if(tistancetocover % D) > 0 :
       steps = (tistancetocover//D)+1

    return steps

print(solution(10, 85, 30))
