def BinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return BinarySearch(alist[:midpoint], item)
            else:
                return BinarySearch(alist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(BinarySearch(testlist, 3))
print(BinarySearch(testlist, 13))