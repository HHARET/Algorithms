"""Given a list of numbers and a number k, return
whether any two numbers from the list add up to K
Ex: Given [10,15,3,7] and k=17 return true since 10+7=17
Bonus: Can you do this in one pass O(N) """
def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False
print two_sum ([98,5,3,8,10],18)