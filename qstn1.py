def addSum(n):
    sum = 0
    for i in range(1, n+1, 1):
        sum += i
    return sum


print(addSum(10))
# Ans -> 55
print(addSum(10000))
# Ans -> 50005000
print(addSum(1000000))
# Ans -> 500000500000
print(addSum(1000000000))
# Ans -> 500000000500000000
