#归并排序
def split_sort(A):
    if len(A)<=1:
        return A
    mid = len(A)//2
    left_sort = A[:mid]
    right_sort = A[mid:]
    ll = split_sort(left_sort)
    rr = split_sort(right_sort)
    return merge_sort(ll,rr)
    
def merge_sort(ll,rr):
    result = []
    i = j = 0
    while i<len(ll) and j<len(rr):
        if ll[i]<=rr[j]:
            result.append(ll[i])
            i=i+1
        else:
            result.append(rr[j])
            j=j+1
    if i==len(ll):
        for n in rr[j:]:
            result.append(n)
    if j==len(rr):
        for n in ll[i:]:
            result.append(n)
    return result
li = [54,26,93,17,77,31,44,55,20]
l2=split_sort(li)
print(l2)


#快速排序
def quick_sort(A, start, end):
    if start<end:
        divindex = partition(A, start, end)
        quick_sort(A, start, divindex)
        quick_sort(A, divindex+1, end)
    else:
        return

def partition(A, start, end):
    i =start-1
    for j in range(start,end):
        if A[end]>=A[j]:
            i = i+1
            A[i],A[j]=A[j],A[i]
    A[i+1], A[end]=A[end],A[i+1]
    return i
li = [54,26,93,17,77,31,44,55,20]
quick_sort(li,0,len(li)-1)
print(li)
