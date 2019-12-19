
def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def maxHeapify(A,i,heapSize):
    l = left(i)
    r = right(i)
    largest = i
    if l<heapSize and A[l]>A[i]:
        largest = l
    if r<heapSize and A[r]>A[largest]:
            largest = r
    if largest != i:
        A[i],A[largest]=A[largest],A[i]
        maxHeapify(A,largest,heapSize)

def buildMaxHeap(A):
    heapSize = len(A)
    for i in range(int(len(A)/2)-1,-1,-1):
        maxHeapify(A,i,heapSize)

def minHeapify(A,i,heapSize):
    l = left(i)
    r = right(i)
    smallest = i
    if l<heapSize and A[l]<A[i]:
        smallest = l
    if r<heapSize and A[r]<A[smallest]:
        smallest = r
    if smallest != i:
        A[i],A[smallest]=A[smallest],A[i]
        minHeapify(A,smallest,heapSize)

def buildMinHeap(A):
    heapSize = len(A)
    for i in range(int(len(A)/2)-1,-1,-1):
        minHeapify(A,i,heapSize)

def heaprevSort(A):
    buildMinHeap(A)
    heapSize=len(A)
    for i in range(len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapSize = heapSize - 1
        minHeapify(A,0,heapSize)

def heapSort(A):
    buildMaxHeap(A)
    heapSize=len(A)
    for i in range(len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapSize = heapSize - 1
        maxHeapify(A,0,heapSize)

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
heapSort(A)
print("Sorted array:")
print(A)
heaprevSort(A)
print("Reverse sorted array:")
print(A)