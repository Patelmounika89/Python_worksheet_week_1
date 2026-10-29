def calculate_bmi(weight_kg,height_m):
    bmi=weight_kg/(height_m**2)
    if bmi >=30:
        categorise='Obese'
    elif bmi >=25 and bmi <=29.9:
        categorise='Overweight'
    elif  bmi>=18 and bmi <=24.9:
        categorise='Normal weight'
    else:
        categorise='Underweight'
    return {"bmi":round(bmi,2),"category":categorise}
print(calculate_bmi(70,1.75))
print(calculate_bmi(90,1.75))
print(calculate_bmi(100,1.75))
print(round(67.8956,2))
