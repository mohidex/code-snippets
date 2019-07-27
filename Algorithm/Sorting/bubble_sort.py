def bubbleSort(alist):
    list_length = len(alist)
    for i in range(list_length):
        for j in range(list_length-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
