def binary_search(list,target):
    first = 0
    last = len(list)-1
    #any programming language is that way 
    # floor division operator //
    while first <= last:
        midpoint = (first+last)//2
       # best case scenario 
       # first is equal to the last 
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index",index)
    else:
        print("Target not found in list")

# if we have the empty loop the while is never activated
numbers= [1,2,3,4,5,6,7,8,9,10]

# if the list not unsorted the binary search may not work

result = binary_search(numbers,6)
verify(result)