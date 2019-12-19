
def lookUpChain(m,p,i,j,s):
    infinity = float("inf")
    if m[i][j] < infinity:
        return m[i][j]
    if i == j:
        m[i][j]=0
    else:
        for k in range(i,j):
            q = lookUpChain(m,p,i,k,s) + lookUpChain(m,p,k+1,j,s)+(p[i-1]*p[k]*p[j])
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
    return m[i][j]

def printParanthesis(s,i,j):
    if i == j:
        print("A{}".format(str(i)),end="")
    else:
        print("(",end="")
        printParanthesis(s,i,s[i][j])
        printParanthesis(s,s[i][j]+1,j)
        print(")",end="")
    
def memoizedMC(p):
    n = len(p) 
    m = [[float("inf") for x in range(n)] for y in range(n)]
    s = [[0 for x in range(n)] for y in range(n)]
    lookUpChain(m,p,1,n-1,s)
    printParanthesis(s,1,n-1)

print("Enter no of matrices:")
n=int(input())
p=[]
for i in range(n):
    print("Enter order of matrix {} in format row column".format(str(i+1)))
    x,y = list(map(int,input().split()))
    if i>0:
        if p[i] != x:
            raise Exception("This is not a valid configuration")
    else:
        p.append(x)
    p.append(y)
memoizedMC(p)
