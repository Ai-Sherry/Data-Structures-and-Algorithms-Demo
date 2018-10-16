#冒泡排序
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                
li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)
#插入排序
def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
li = [54,26,93,17,77,31,44,55,20]
insertion_sort(li)
print(li)
#选择排序
def selection_sort(array):
    for i in range(len(array)):
        mymin=array[i]
        min_index=i
        for j in range(i,len(array)):
            if array[j]<mymin:
                mymin=array[j]
                min_index=j
        array[min_index],array[i]=array[i],array[min_index]
li = [54,26,93,17,77,31,44,55,20]
selection_sort(li)
print(li)
