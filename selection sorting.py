a=[4,2,23,45,43,35,8,6,5,1]
for i in range(len(a)):
	min=a[i]
	loc=i
	for j in range(i+1,len(a)):
		if a[j]<min:
			min=a[j]
			loc=j
	a[i],a[loc]=a[loc],a[i]
print(a)

==> O(n^2)
