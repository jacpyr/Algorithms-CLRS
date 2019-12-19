def findMaxCrossingSubarray(A,low,mid,high):
    leftSum = float("-inf")
    _sum = 0
    maxLeft = low
    for i in range(mid,low-1,-1):
        _sum = _sum + A[i]
        if _sum > leftSum:
            leftSum = _sum
            maxLeft = i
    rightSum = float("-inf")
    _sum = 0
    maxRight = low
    for i in range(mid+1,high+1):
        _sum = _sum + A[i]
        if _sum > rightSum:
            rightSum = _sum
            maxRight = i
    return (maxLeft,maxRight,leftSum+rightSum)

def findMaxSubArray(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:
        mid = (low+high) // 2
        lLow,lHigh,lSum = findMaxSubArray(A,low,mid)
        rLow,rHigh,rSum = findMaxSubArray(A,mid+1,high)
        crossLow,crossHigh,crossSum = findMaxCrossingSubarray(A,low,mid,high)
        maxSum = max(lSum,rSum,crossSum)

        if(maxSum==lSum):
            return (lLow,lHigh,lSum)
        elif(maxSum==lSum):
            return (rLow,rHigh,rSum)
        else:
            return (crossLow,crossHigh,crossSum)

A = list(map(int,list("13 -3 -25 20 -3 -16 -23 18 20 -7 12 -5 -22 15 -4 7".split())))
#A=list(input().split())
low,high,maxSum = findMaxSubArray(A,0,len(A)-1)
print("Sorted array:")
print(A[low:high+1])
print("Max Sum = {}".format(str(maxSum)))