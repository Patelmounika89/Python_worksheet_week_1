def convert_case(text,case_type):
    uppercase=text.upper()
    lowercase=text.lower()
    titlecase=text.title()
    if case_type=='upper':
        return uppercase
    elif case_type=='lower':
        return lowercase
    elif case_type=='title':
        return titlecase
    else:
        return "Invalid case_type"
print(convert_case('hello world','upper'))
print(convert_case('HELLO WORLD','lower'))
print(convert_case('hello world','title'))
print(convert_case('hello world','caps'))