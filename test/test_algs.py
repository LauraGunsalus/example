import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():

    # Negatives, even
    (sortedL, con, asg) = algs.bubblesort(np.array([-2,2,-51,0]))
    assert(np.array_equal(sortedL, np.array([-51,-2,0,2])))

    # Odd
    (sortedL, con, asg) = algs.bubblesort(np.array([-2,2,-51]))
    assert(np.array_equal(sortedL, np.array([-51,-2,2])))

    # Duplicates
    (sortedL, con, asg) = algs.bubblesort(np.array([1,1,1]))
    assert(np.array_equal(sortedL, np.array([1,1,1])))
    
    # Empty
    (sortedL, con, asg) = algs.bubblesort(np.array([]))
    assert(np.array_equal(sortedL, np.array([])))

    # Characters
    (sortedL, con, asg) = algs.bubblesort(np.array(['a','d','b','c','a']))
    assert(np.array_equal(sortedL, np.array(['a','a', 'b','c','d'])))

    # Strings
    (sortedL, con, asg) = algs.bubblesort(np.array(['cca','aac','aab','aca','aaa']))
    assert(np.array_equal(sortedL, np.array(['aaa','aab','aac','aca','cca'])))

    # Sorted
    (sortedL, con, asg) = algs.bubblesort(np.array([1,2,3]))
    assert(np.array_equal(sortedL, np.array([1,2,3])))

    # Reverse Sorted
    (sortedL, con, asg) = algs.bubblesort(np.array([3,2,1]))
    assert(np.array_equal(sortedL, np.array([1,2,3])))


def test_quicksort():

    # Negatives, even
    (sortedL, con, asg) = algs.quicksort(np.array([-2,2,-51,0]))
    assert(np.array_equal(sortedL, np.array([-51,-2,0,2])))

    # Odd
    (sortedL, con, asg) = algs.quicksort(np.array([-2,2,-51]))
    assert(np.array_equal(sortedL, np.array([-51,-2,2])))

    # Duplicates
    (sortedL, con, asg) = algs.quicksort(np.array([1,1,1]))
    assert(np.array_equal(sortedL, np.array([1,1,1])))
    
    # Empty
    (sortedL, con, asg) = algs.quicksort(np.array([]))
    assert(np.array_equal(sortedL, np.array([])))

    # Characters
    (sortedL, con, asg) = algs.quicksort(np.array(['a','d','b','c','a']))
    assert(np.array_equal(sortedL, np.array(['a','a', 'b','c','d'])))

    # Sorted
    (sortedL, con, asg) = algs.quicksort(np.array([1,2,3]))
    assert(np.array_equal(sortedL, np.array([1,2,3])))

    # Reverse Sorted
    (sortedL, con, asg) = algs.quicksort(np.array([3,2,1]))
    assert(np.array_equal(sortedL, np.array([1,2,3])))
