def find_min_index(arr):
    """ Helper function to find the index of the minimum element in the list. """
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def mySort(l):
    """ Sorts a list using the Selection Sort algorithm. """
    lc = l.copy()  # Copy of the list to avoid modifying the original list
    s = []  # Sorted list

    while lc:
        min_index = find_min_index(lc)
        s.append(lc[min_index])
        lc.pop(min_index)
    
    return s

def find_min_abs_index(list):
    """Helper Function to find the index of minimum absolute element of the list"""
    min_abs_index = 0
    for i in range (1, len(list)):
        if abs(list[i]) < abs(list[min_abs_index]):
            min_abs_index = i
    return min_abs_index

def mySortAbs(l):
    """Sorts the list by selction sort using the selection sort algorthm"""
    lc = l.copy()
    s = []
    while lc :
        min_abs_index = find_min_abs_index(lc)
        s.append(lc[min_abs_index])
        lc.pop(min_abs_index)  

    return s

def main():
    print(mySort([35,-49,43,105,-88,87,86]))
    print(mySortAbs([35,-49,43,105,-88,87,86]))
if __name__ == "__main__":
	main()