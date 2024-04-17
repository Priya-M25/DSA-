def removeDuplicates(arr, n):
    # Edge case: If the array is empty, return 0
    if n == 0:
        return 0
    
    # Initialize a counter to count unique elements
    unique_count = 1
    
    # Iterate through the array starting from the second element
    for i in range(n-1):
        # If the current element is different from the previous element,
        # increment the unique_count
        if arr[i] != arr[i + 1]:
            unique_count += 1
    
    return unique_count

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
n = len(arr)
unique_count = removeDuplicates(arr, n)
print("Number of unique elements:", unique_count)


'''OUTPUT :-
Number of unique elements: 5
'''

