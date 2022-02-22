def grade_student(grades):
    """
    seperaing the algorithm for rounding a student grades into a seperate 
    function then calls the algorithm on the array of grdades returning 
    a new array of the rounded grades.
    Time Complexity -> O(n)
    Space Complexity
    """
    def rounding_algo(grade):
        if grade < 38:
            return grade
        rounded_grade = 5 * round(grade/5)
        if rounded_grade < grade:
            return grade
        return rounded_grade
    # applies the rounding algorithm on every grade in the grades array
    # returning a new array of the rounded grades.
    return [rounding_algo(grade) for grade in grades]


print(grade_student([84, 38, 57]))
