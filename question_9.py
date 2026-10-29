def calculate_total(price,discount_percent=0):
    subtotal=sum(price)
    discount_amount=(subtotal*discount_percent)/100
    final_total=subtotal-discount_amount
    return {"subtotal":subtotal,"discount_amount":discount_amount,"total":final_total}
print(calculate_total([50,30,45,25]))
print(calculate_total([50,30,45,25],10))
print(calculate_total([50,30,45,25],20))