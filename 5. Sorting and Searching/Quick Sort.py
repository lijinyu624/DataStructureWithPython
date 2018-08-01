def QuickSort(alist, first, last):
    if first < last:
        pivot = partition(alist, first, last)
        QuickSort(alist, first, pivot-1)
        QuickSort(alist, pivot+1, last)
    return alist

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
print(QuickSort(alist, 0, len(alist)-1))