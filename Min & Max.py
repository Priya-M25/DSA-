def getMinMax(a, n):
    if n == 1:
        return None,None
    min_val = max_val = a[0]
    for i in a[1:]:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    return min_val, max_val
def main():
  T = int(input())
  while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])
        T -= 1
if __name__ == "__main__":
    main()


--------------------
#2nd code

a=[3,1,7,15,11]
l=h=0
te=t=a[0]
for i in range(len(a)):
    if a[i]<t:
        t=a[i]
        l=t
    if a[i]>te:
        te=a[i]
        h=te
print("Low =",l)
print("high =",h)
