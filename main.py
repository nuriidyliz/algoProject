import time
import sys
sys.setrecursionlimit(2001)
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def merge(arr, l, m, r):
    n1 = (int)(m - l + 1)
    n2 = (int)(r - m)

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[(int)(l + i)]

    for j in range(0, n2):
        R[j] = arr[(int)(m + 1 + j)]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(1001)]


    # Store count of each character

    for i in arr:
        if type(i) == str:
            print(i);
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i - 1]

        # Build the output character array
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        arr[i] = output[i]

smallAscText = open("Sets/1k_Ascending.txt","r")
smallDescText = open("Sets/1k_Descending.txt","r")
smallRandText = open("Sets/1k_Random.txt","r")
smallAscText2 = open("Sets/2k_Ascending.txt","r")
smallDescText2 = open("Sets/2k_Descending.txt","r")
smallRandText2 = open("Sets/2k_Random.txt","r")
mediumAscText = open("Sets/10k_Ascending.txt","r")
mediumDescText = open("Sets/10k_Descending.txt","r")
mediumRandText = open("Sets/10k_Random.txt","r")
largeAscText = open("Sets/20k_Ascending.txt","r")
largeDescText = open("Sets/20k_Descending.txt","r")
largeRandText = open("Sets/20k_Random.txt","r")
xLargeAscText = open("Sets/30k_Ascending.txt","r")
xLargeDescText = open("Sets/30k_Descending.txt","r")
xLargeRandText = open("Sets/30k_Random.txt","r")

smallAscArr =smallAscText.read().split(',')
smallAscArr = list(map(int,smallAscArr))

smallDescArr =smallDescText.read().split(',')
smallDescArr = list(map(int,smallDescArr))

smallRandArr =smallRandText.read().split(',')
smallRandArr = list(map(int,smallRandArr))

smallAscArr2 =smallAscText2.read().split(',')
smallAscArr2 = list(map(int,smallAscArr2))

smallDescArr2 =smallDescText2.read().split(',')
smallDescArr2 = list(map(int,smallDescArr2))

smallRandArr2 =smallRandText2.read().split(',')
smallRandArr2 = list(map(int,smallRandArr2))

mediumAscArr =mediumAscText.read().split(',')
mediumAscArr = list(map(int,mediumAscArr))

mediumDescArr =mediumDescText.read().split(',')
mediumDescArr = list(map(int,mediumDescArr))

mediumRandArr =mediumRandText.read().split(',')
mediumRandArr = list(map(int,mediumRandArr))

largeAscArr =largeAscText.read().split(',')
largeAscArr = list(map(int,largeAscArr))

largeDescArr =largeDescText.read().split(',')
largeDescArr = list(map(int,largeDescArr))

largeRandArr =largeRandText.read().split(',')
largeRandArr = list(map(int,largeRandArr))

xLargeAscArr = xLargeAscText.read().split(',')
xLargeAscArr = list(map(int,xLargeAscArr))

xLargeDescArr = xLargeDescText.read().split(',')
xLargeDescArr = list(map(int,xLargeDescArr))

xLargeRandArr = xLargeRandText.read().split(',')
xLargeRandArr = list(map(int,xLargeRandArr))

smallAscText.close()
smallDescText.close()
smallRandText.close()
smallAscText2.close()
smallDescText2.close()
smallRandText2.close()
mediumAscText.close()
mediumDescText.close()
mediumRandText.close()
largeAscText.close()
largeDescText.close()
largeRandText.close()
xLargeAscText.close()
xLargeDescText.close()
xLargeRandText.close()

setArr = [smallAscArr,smallDescArr,smallRandArr, smallAscArr2, smallDescArr2, smallRandArr2,
          mediumAscArr,mediumDescArr,mediumRandArr,largeAscArr,largeDescArr, largeRandArr,
          xLargeAscArr, xLargeDescArr, xLargeRandArr]
setName = ["1k_Ascending", "1k_Descending", "1k_Random",
           "2k_Ascending", "2k_Descending", "2k_Random",
           "10k_Ascending", "10k_Descending", "10k_Random",
           "20k_Ascending", "20k_Descending", "20k_Random",
           "30k_Ascending", "30k_Descending", "30k_Random"]
print(setArr[8])
quickSort(setArr[8], 0 , len(setArr[8]) -1)
print(setArr[8])

for i in range(0, len(setArr)):
    print("-----Set: "+  setName[i] +" Time Measurements-----")
    print(setArr[i])
    startTime = time.time()
    insertionSort(setArr[i])
    endTime = time.time()
    execTime = (endTime - startTime) * 100
    print("Insertion Sort Execution Time: ", str(execTime))

    startTime = time.time()
    mergeSort(setArr[i], 0 , len(setArr[i]) -1)
    endTime = time.time()
    execTime = (endTime - startTime) * 100
    print("Merge Sort Execution Time: ", str(execTime))

    try :
        startTime = time.time()
        quickSort(setArr[i], 0 , len(setArr[i]) -1)
        endTime = time.time()
        execTime = (endTime - startTime) * 100
        print("Quick Sort Execution Time: ", str(execTime))

    except RecursionError:
        print("Quick Sort Recursion Error")


    startTime = time.time()
    heapSort(setArr[i])
    endTime = time.time()
    execTime = (endTime - startTime) * 100
    print("Heap Sort Execution Time: ", str(execTime))

    startTime = time.time()
    countSort(setArr[i])
    endTime = time.time()
    execTime = (endTime - startTime) * 100
    print("Count Sort Execution Time: ", str(execTime))

    print()