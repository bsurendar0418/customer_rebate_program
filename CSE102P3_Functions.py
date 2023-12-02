menu="""
------------------------ 
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program 
------------------------"""
def Display_Menu():
    print(menu)
    option=input("Enter Menu Option: ")
    return option

def GetNextCustomerID(customerfilename):
    next_id=None
    try:
        with open(customerfilename) as f:
            lines=f.readlines()

        last_id=lines[-1][:6]

        next_id=int(last_id)+1
        
    except FileNotFoundError as e:
        print("Exception: %s" % e)
    return next_id

def GetNextRebateID(rebatefilename):
    next_id=None
    try:
        with open(rebatefilename) as f:
            lines=f.readlines()

        last_id=lines[-1][1:8]
        next_id=int(last_id)+1
    except FileNotFoundError as e:
        print("Exception: %s" % e)
    return next_id

