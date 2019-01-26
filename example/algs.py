import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    assignments = 0
    conditionals = 0
    for i in range(len(x)):
        assignments += 1
        for j in range(1, len(x)):
            assignments += 1
            if (x[j-1] > x[j]):
                conditionals += 1
                x[j-1], x[j] = x[j], x[j-1]
                assignments += 2
    return (x, assignments, conditionals)


def quicksort(x):
    global conditional
    global assignment
    conditional = 0
    assignment = 0
    quicksortRun(x, 0, len(x)-1),
    return x, conditional, assignment

def quicksortRun(L, lo, hi):
    global conditional
    global assignment
    if lo < hi:
        conditional += 1
        p = partition(L, lo, hi)
        assignment += 1
        quicksortRun(L, lo, p-1)
        quicksortRun(L, p+1, hi)
    return L

def partition(L,lo,hi):
    global conditional
    global assignment
    pivot = L[hi] 
    assignment += 1
    i = lo-1 
    assignment += 1        
    for j in range(lo, hi): 
        assignment += 1
        if (L[j] <= pivot): 
            conditional += 1
            i += 1
            assignment += 1
            L[i],L[j] = L[j],L[i] 
            assignment += 2
    L[i+1],L[hi] = L[hi],L[i+1] 
    assignment += 2
    newPivot = i+1
    assignment += 1
    return newPivot
