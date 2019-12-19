def partition(A,s,e):
    x = A[e]
    i = s - 1
    for j in range(s,e):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[e] = A[e], A[i+1]
    return (i + 1)

def quickSort(A,s,e):
    if s<e:
        m = partition(A,s,e)
        quickSort(A,s,m-1)
        quickSort(A,m+1,e)

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
quickSort(A,0,len(A)-1)
print("Sorted array:")
[print(a,end=" ") for a in A]