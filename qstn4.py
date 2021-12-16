def getSuperDigit(n, k):
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
