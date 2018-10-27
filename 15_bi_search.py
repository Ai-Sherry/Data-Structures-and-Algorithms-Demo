#二分查找
def b_search(A,n,value):
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if A[mid]==value:
            return mid
        elif A[mid]<value:
            low=mid+1
        else:
            high=mid-1
    return -1

A=[0,1,2,3,4,5,6]
n=7
value=4
c=b_search(A,n,value)
print(c)
