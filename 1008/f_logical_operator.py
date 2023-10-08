# AND: both
# OR: at least one
# NOT: 


has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Uneligible for loan. Sorry")
    
    

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Uneligible for loan. Sorry")
    
has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Uneligible for loan. Sorry")