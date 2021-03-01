# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108


while principal > 0 :
    
    principal = principal * (1+rate/12) - payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra
        total_paid += payment + extra
    else :
        total_paid += payment
    
    print(f"{month} {round(total_paid,2)} {round(principal,2)}")
    month += 1 
print(f"{month}") 
print('Total paid',round(total_paid,2))
