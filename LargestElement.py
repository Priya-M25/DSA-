def largestElement(arr: [], n: int) :
    maxn = arr[0] 
    for i in range(1, len(arr)):  
        if maxn < arr[i]:  
            maxn = arr[i]  
    return maxn

# Example usage
arr = [1, 5, 3, 9, 2]
n = len(arr)
largest = largestElement(arr, n)
print("Largest element in the array:", largest)

'''OUTPUT :-
Largest element in the array: 9
'''
