#Write a Python function, calculate_final_price, that takes the following inputs:
#• base_price (float): The original price of the product.
#• discount_percentage (float): The percentage discount to be applied (default is 0%).
#• tax_percentage (float): The percentage tax to be applied (default is 0%).
#the function should:
#• Return the final price of the product, rounded to two decimal places.
#• Include error handling to ensure that negative values for base_price, discount_percentage, 
#or tax_percentage raise a ValueError
base_price=float(input())
discount_percentage=float(input())
tax_percentage=float(input())
def calculate_final_price(base_price,discount_percentage,tax_percentage):
    if base_price<0 and discount_percentage<0 and tax_percentage<0:
        return 'Error'
    else:
        discountper=base_price*discount_percentage/100
        tot_discount=base_price-discountper
        tax=tax_percentage/100*tot_discount
        total=tot_discount+tax
        return round(total,2)
result=calculate_final_price(base_price,discount_percentage,tax_percentage)
print( result)

    
    
    
    

