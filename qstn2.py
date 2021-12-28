def gradeStudent(grades):
    """
    seperaing the algorithm for rounding a student grades into a seperate 
    function then calls the algorithm on the arrya of grdades returning 
    a new array of the rounded grades.
    Big O -> O(n)
    """
    def roundingAlgo(grade):
        if grade < 38:
            return grade
        roundedGrade = 5 * round(grade/5)
        if roundedGrade < grade:
            return grade
        return roundedGrade
    return [roundingAlgo(grade) for grade in grades]


print(gradeStudent([84, 38, 57]))
