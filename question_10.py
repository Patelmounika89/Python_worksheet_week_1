def validate_password(password):
    errors=[]
    if len(password)<8:
        errors.append("At least 8 characters required")
    if not any(char.isupper()
        for char in password):
        errors.append("UpperCase letter requried")
    if not any(char.islower()
        for char in password):
        errors.append("LowerCase letter requried")
    if not any(char.isdigit()
        for char in password):
        errors.append("Digit requried")
    special_chars="!@#$%^&*"
    if not any(char in special_chars 
        for char in password):
        errors.append("Special Character requried")
    return{"is_valid":len(errors)==0,"errors":errors}
print(validate_password("weak"))
print(validate_password("Weak123"))
print(validate_password("MySecure@1"))