"""Given a list of numbers and a number k, return
whether any two numbers from the list add up to K
Ex: Given [10,15,3,7] and k=17 return true since 10+7=17
Bonus: Can you do this in one pass """

"""Solution 1 Brute force O(N2)"""
def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            	if i != j and lst[i] + lst[j] == k:
                	return True
    return False

print two_sum([3,2,5,7,3],19)
