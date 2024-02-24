arr = [2, 5, 1, 10, 15, 90]
temp=t= arr[0]
n = len(arr)
low, high = 0, 0
h = []
k = 3
for i in range(1, n):
    if arr[i] < temp:
        temp = arr[i]
        low= temp
    if arr[i] > t:
        t = arr[i]
        h.append(t)
if k <= n:
    kth_max = h[k - 1]
print('low = ', low)
print('kth max = ', kth_max)