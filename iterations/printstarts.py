def printstars(N):
    for i in range(1,N+1):
        str=""
        for j in range(i):
            str=str+"*"
            #print str

        print str
def printstarsShort(N):
    str=""
    for i in range(1,N+1):
        str="*"*i
        print str

def upsideDown(n):
    spc=""
    for i in range (n,0,-1):
        spc+="   "
        st=spc+""
        for j in range(2*i,1,-1):
            st+=" * "
        print st

def upsideDownShort(n):
    spc=""
    for i in range (n,0,-1):
        spc+="   "
        st=""
        l = (2*i)-1
        st =spc+ " * " * l
        print st



printstars(4)
printstarsShort(4)
upsideDown(4)
upsideDownShort(4)
