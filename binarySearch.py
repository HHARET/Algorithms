""" Steps to binary search [1,3,5,3,7,2,9]
1-The Array must be sorted MUST BE SORTED
2- define the initial values (the starting point
and the ending point of the array) 
3- While first element of the array<= 
	last elemnt of the array we will be still looking
4- we establish the middle element (it has to be integer)
5- we compare the middle element if it is what we are looking for
6- if not we have to establish wich side we will be looking at
7 if the element if larger then we have to move the
 first element to replace the middle element and add 1
 if it is smaller we have to move the last element to the middle
 and subtract 1"""

def binarySearch(array,num):
	array.sort()
	first=0
	last=len(array)-1
	while first<=last:
		mid = int((first+last)/2)
		if array[mid] == num:
			print "yyyyyyyyyyyyyyyyyyyyyyyyyy"
			print array[mid]
			return mid
		if array[mid]>num:
			last = mid-1
		else:
			first= mid+1
		pass
	return False

print binarySearch([5,4,4,6,7],6)



