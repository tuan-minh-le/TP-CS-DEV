def mesImpots(income) :
    taxes = 0
    if income >= 160337 :
        income - income - 160337
        taxes = income*(45/100) + (160336 - 74546)*0.41 + (74545-26071)*0.3 + (26070-10226)*0.11
    elif income >= 74546 and income <= 160336 :
        income = income - 74546
        taxes = income*(41/100) + (74545-26071)*0.3 + (26070-10226)*0.11
    elif income >= 26071 and income <= 74545 :
        income = income - 26071
        taxes = income*(30/100) + (26070-10226)*0.11
    elif income >= 10226 and income <= 26070 :
        income = income - 10226
        taxes = income*(11/100) 
    return int(taxes)

def principal():
    income = input ("QUel est votre salaire annuel ? : ")
    mesImpots(income)
    