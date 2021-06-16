def insertion_sort(A):
    for j in range(1,len(A)):
        i=j-1
        key=A[j]
        while(i>-1 and A[i]>key):
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    return A
print(insertion_sort([4,3,2,7,8,6]))
==>O(n^2) and omega(n)
