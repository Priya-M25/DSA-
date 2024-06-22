arr=[4,12,5,3,1,2,5,3,1,2,4,6]
op=[-1]*len(arr)
st=[]
for i in range(len(arr)-1,-1,-1):
    while st and st[-1]<=arr[i]:
        st.pop()
    if st:
        op[i]=st[-1]
    else:
        op[i]=-1
    st.append(arr[i])
print(op)


''' OUTPUT :-
[12, -1, 6, 5, 2, 5, 6, 4, 2, 4, 6, -1]
'''
