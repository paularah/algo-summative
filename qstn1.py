def add_sum(n):
    """
    iterate over every value up to n and continouly add to a temporary value 
    Time Complexity -> O(n)
    Space Complexity -> O(n)
    """
    sum = 0
    for i in range(1, n+1, 1):
        sum += i
    return sum


print(add_sum(10))
# Ans -> 55
print(add_sum(10000))
# Ans -> 50005000
print(add_sum(1000000))
# Ans -> 500000500000
print(add_sum(1000000000))
# Ans -> 500000000500000000
