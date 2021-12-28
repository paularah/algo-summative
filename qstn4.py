def getSuperDigit(n, k):
    """
    Iteratively calls the algorith for calulTting the super on n repated k times
    untile the value is a single digit. Tis could also be done the recursive and the single
    condition can be used as the base case.
    """
    def superDigit(digit):
        while len(str(digit)) != 1:
            strDigit = str(digit)
            nextDigit = 0
            for char in strDigit:
                nextDigit += int(char)
            digit = nextDigit
        return digit
    result = superDigit(int(n * k))
    return result


print(getSuperDigit('148', 3))
