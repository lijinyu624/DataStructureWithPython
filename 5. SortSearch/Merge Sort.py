def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j <len(right):
        if (left[i]<right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result += left[i:]
    result += right[j:]
    # += different from .append()
    # list + list?
    print("left: ", left)
    print("right: ", right)
    print ("result: ", result)
    return result

def MergeSort(alist):
    if (len(alist) <= 1):
        return alist
    mid = len(alist) // 2
    left = MergeSort(alist[:mid])
    right = MergeSort(alist[mid:])
    return merge(left, right)

alist = [54,26,93,17,77,31,44,55,20]
result = MergeSort(alist)
print(result)