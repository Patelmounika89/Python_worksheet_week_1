def assign_grade(score):
    if score >100 or score < 0:
        return "Invalid Score"
    elif score >=90 and score <=100:
        return "A"
    elif score >=80 and score <=89:
        return "B"
    elif score >=70 and score <=79:
        return "C"
    elif score >=60 and score <=69:
        return "D"
    else:
        return "F"
print(assign_grade(95))
print(assign_grade(85))
print(assign_grade(75))
print(assign_grade(65))
print(assign_grade(55))
print(assign_grade(105))