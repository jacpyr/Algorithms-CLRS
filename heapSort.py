
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

def heapSort(A):
    buildMaxHeap(A)
    heapSize=len(A)
    for i in range(len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapSize = heapSize - 1
        maxHeapify(A,0,heapSize)

print("Enter an array to Sort (numbers seperated by space):")
A=list(map(int,input().split()))
heapSort(A)
print(A)