def merge(A,s,m,e):
    L=[]
    R=[]
    
    for i in range(s,m+1):
        L.append(A[i])
    for i in range(m+1,e+1):
        R.append(A[i])
    n1=len(L)
    n2=len(R)
    L.append(float('inf'))
    R.append(float('inf'))
    i,j = 0,0
    
    for k in range(s, e + 1):
        if(L[i]<=R[j]):
            A[k]=L[i]
            i = i + 1
        else:
            A[k]=R[j]
            j = j + 1
    
def mergeSort(A,s,e):
    if s < e:
        m = (s+e) // 2
        mergeSort(A,s,m)
        mergeSort(A,m+1,e)
        merge(A,s,m,e)

print("Enter an array to Sort (elements seperated by space):")
A=list(input().split())
numeric = True
for a in A:
    if not a.isnumeric():
        numeric=False
        break
if(numeric):
    A=list(map(int,A))
else:
    try:
        A=list(map(float,A))
    except:
        pass
mergeSort(A,0,len(A)-1)
print("Sorted array:")
print(A)