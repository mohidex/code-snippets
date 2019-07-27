def selectionSort(alist):
    length = len(alist)
    for i in range(length):
        for j in range(i+1, length):
            if alist[j] < alist[i]:
                min = alist[j]
                alist[j], alist[i] = alist[i], min
