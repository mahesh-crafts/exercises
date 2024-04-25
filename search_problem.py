import timeit

def bruteforce_solution(input_size, target):
    """
    Given a list of numbers sorted in increasing order and a target number, find the target number in the list.
    If the target number is found in the list, return True. Otherwise, return False.
    """
    start = 0
    input = [i for i in range(start, input_size + 1)]
    
    for i in range(input_size):
        if input[i] == target:
            print("Target found at index:", i)
            return
            
    print("Target not found")
    return


def optimal_solution(input_size, target):
    """
    Given a list of numbers sorted in increasing order and a target number, find the target number in the list.
    If the target number is found in the list, return True. Otherwise, return False.
    """
    pass


input_size = 1000000000
target = 999999999

print("Array size:", input_size)
print("Target:", target)

print("bruteforce_solution")
print("Execution Time:", timeit.timeit(lambda: bruteforce_solution(input_size, target), number=1))

print("optimal_solution")
print("Execution Time:", timeit.timeit(lambda: optimal_solution(input_size, target), number=1))

print("-" * 30)
