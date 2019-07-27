#Python program for implementing insertion sort

def insertionSort(alist):
    
    #Traverse through 1 to n
    for i in range(1, len(alist)):
       
        key = alist[i]
        
        """ Move element of alist[0...i-1], that are greater than key,
        to oen position ahead of their current position  """
        
        j = i-1
        while j >= 0 and key < alist[j]:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key
