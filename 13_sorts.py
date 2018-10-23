#计数排序
def count_sort(A):
#1.列出数列的最大值和最小值
    mmax=A[0]
    mmin=A[0]
    for i in range(1,len(A)):
        if mmax<A[i]:
            mmax=A[i]
        if mmin>A[i]:
            mmin=A[i]
    d=mmax-mmin
#2.创建统计数组并统计对应整数个数
    print(d)
    out=[]
    out = [0 for x in range(0,d+1)]
    sort=[]
    sort=[0 for x in range(0,len(A))]
    for i in range(len(A)):
        out[A[i]-mmin]=out[A[i]-mmin]+1
#3.统计数组做变形，后面的元素等于前面的元素之和
    for i in range(1,len(out)):
        out[i]=out[i-1]+out[i]
#4.倒序遍历原始序列
    for i in range(len(A)-1,-1,-1):
        index=out[A[i]-mmin]-1
        sort[index]=A[i]
        out[A[i]-mmin]=out[A[i]-mmin]-1
    return sort
A=[91,93,91,95,94,99,95]
B=count_sort(A)
print(B)
