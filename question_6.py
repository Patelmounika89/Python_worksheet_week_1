def separate_even_odd(numbers):
    even_list=[]
    odd_list=[]
    for list in numbers:
        if list%2==0:
           even_list.append(list)
        else:
           odd_list.append(list)
    return "Even:",even_list,"Odd:",odd_list
   
print(separate_even_odd([1,2,3,4,5,6,7,8,9,10]))