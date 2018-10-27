#二分查找—查找第一个等于给定值的元素
def b_search_1(A,value):
    n=len(A)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if A[mid]<value:
            low=mid+1
        elif A[mid]>value:
            high=mid-1
        else:
            if mid==0 or A[mid-1]!=value:
                return mid
            else:
                high=mid-1
    return -1

A=[0,1,2,3,4,5,5,5,5,6]

value=5
c=b_search_1(A,value)
print(c)

#二分查找—查找最后一个等于给定值的元素
def b_search_2(A,value):
    n=len(A)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if A[mid]<value:
            low=mid+1
        elif A[mid]>value:
            high=mid-1
        else:
            if mid==n-1 or A[mid+1]!=value:
                return mid
            else:
                low=mid+1
    return -1

A=[0,1,2,3,4,5,5,5,5,6]

value=5
c=b_search_2(A,value)
print(c)

#二分查找—查找第一个大于等于给定值的元素
def b_search_3(A,value):
    n=len(A)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if A[mid]>=value:
            if mid==0 or A[mid-1]<value:
                return mid
            else:
                high=mid-1
        else:
            low=mid+1
    return -1

A=[0,1,2,3,4,5,5,5,5,6]

value=5
c=b_search_3(A,value)
print(c)

#二分查找—查找最后一个小于等于给定值的元素
def b_search_4(A,value):
    n=len(A)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if A[mid]<=value:
            if mid==n-1 or A[mid+1]>value:
                return mid
            else:
                low=mid+1
        else:
            high=mid-1
    return -1

A=[0,1,2,3,4,5,5,5,5,6]

value=5
c=b_search_4(A,value)
print(c)
