"""
Function to get the income tax imposed on ones earnings
in the UK

consider: 
If earnings < 12000 per year, pay no tax
then with earnings between 12,000 and 36,000 pay 20% tax
then with earnings greater than 36000 per year, pay 40% tax

"""

def tax_calc1(income):
    return 0

def tax_calc2(income):
    if income > 0:
        return 0
    else:
        pass

def tax_calc3(income):
    if income <= 12000:
        tax = 0
    else:
        pass
    return tax

# Modify to cater for income above 36,000
def tax_calc4(income):
    """Fix me:Negative values return wrong value"""
    tax = 0
    if income <= 12000: # first band  of income
        tax = 0
    elif income <= 36000: # second band 12000 to 36000
        tax = (income - 12000) * 0.2
    elif income > 36000: # third band of 36000 to infinity
        tax = (24000 * 0.2) + ((income - 36000) * 0.4)
    #elif income < 0:
        #return 0
    else:
        pass
    return tax