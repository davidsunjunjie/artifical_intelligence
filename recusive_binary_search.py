def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else: 
            if list[midpoint] < target:
              return recursive_binary_search(list[midpoint+1:],target)
            else:
             return recursive_binary_search(list[:midpoint],target)  
#tail call optimization 
def verify(result):
    print("Target Found",result)

numbers= [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers,12)
verify(result)

result = recursive_binary_search(numbers,6)
verify(result)
#algorithm thinking break the problem into concrete input and output, along with distinct set of steps that solves 
# the problem by going from input to output.learn algorithm payoff in the long run.
# The steps in the algorithm need to be in a very specific order
# The Steps also need to be distinct
# The algorithm should produce a result
# The algorithm should complete in a finite amount of time 
# Time complexity 
# Space complexity 