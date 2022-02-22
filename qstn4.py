def get_super_digit(n, k):
    """
    Iteratively calls the algorithm for calcuting the super on n repated k times
    until the value is a single digit. This could also be done the recursive and the single
    condition can be used as the base case.
    Time Complexity -> O(n)
    Space Complexity -> O(n)
    """
    # seperate the algorithm for calculting the super digit into a different fuction
    def super_digit(digit):
        # checks  that string version of the digit is not a single character
        while len(str(digit)) != 1:
            # converts the digit into a string
            str_digit = str(digit)
            # initialize a variable to keep ltrack of the next digit
            next_digit = 0
            # loops through every character in the string version digit and
            # conberts this to a string then adds it to the next digit variable
            for char in str_digit:
                next_digit += int(char)
            # make the next digit the new digit returns it
            digit = next_digit
        return digit
    # calls the super digit function on n repeated k times
    result = super_digit(int(n * k))
    return result


print(get_super_digit('148', 3))
