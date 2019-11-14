# https://www.geeksforgeeks.org/selection-sort/
# Selection sort works by repeatedly "selecting" the next-smallest
# element from the unsorted array and moving it to the front.


def selectionSort(arr):
    l = len(arr)
    temp = -1
    l_ind = -1
    for i in range(l):
        l_ind=i
        for j in range(i, l):
            if arr[j] < arr[l_ind]:
                l_ind = j
        temp = arr[l_ind]
        arr[l_ind]=arr[i]
        arr[i]=temp
    return arr

arr=[13,1,45,22,56,88,3,12,45,46,22,77,43]
print(selectionSort(arr))

# TC :O(n^2) This is cz there are 2 loops
# SC: O(n) cz it's happening in the same array