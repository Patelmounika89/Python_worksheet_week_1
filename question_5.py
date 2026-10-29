def count_items(items_list):
    freq={}
    for key in items_list:  
       freq[key]= freq.get(key,0)+1
    return freq    
print(count_items(["apple","banana","apple","cherry","banana","apple"])) 