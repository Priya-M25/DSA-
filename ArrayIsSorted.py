def isSorted(n: int, a: [int]) -> int:
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return 0  
    return 1  

# Sample list (sorted)
numbers = [1, 3, 5, 7, 9]

# Call the function
is_sorted = isSorted(len(numbers), numbers)

# Check the return value
if is_sorted == 1:
  print("The list is sorted!")
else:
  print("The list is not sorted.")

'''Output :-
The list is sorted!
'''
