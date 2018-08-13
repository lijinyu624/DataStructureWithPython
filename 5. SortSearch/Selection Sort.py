def SelectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for position in range(1, fillslot+1):
            if alist[position] > alist[positionOfMax]:
                positionOfMax = position

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
SelectionSort(alist)
print(alist)