# คำนวณภาษี
salary_1 = 15000
tax = 0.07
ot_time = 10
ot_rate = 200

gross_pay = salary + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay_2 = gross_pay - tax_pay

print(f"{net_pay}") 

# คำนวณภาษี 2
salary_2 = 15000
tax = 0.07
ot_time_2 = 10
ot_rate_2 = 200

gross_pay = salary_2 + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay_2 = gross_pay - tax_pay

print(f"{net_pay}")
