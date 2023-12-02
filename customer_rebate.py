import sys
import threading
from CSE102P3_Functions import *

# Create a lock object
lock = threading.Lock()

#synchronized lists
id=[]
names=[]
emails=[]
rebate_id=[]
cust_id=[]
purch_date=[]
purch_amt=[]
submit_date=[]
expect_rebate_amt=[]
approved=[]
approve_date=[]
approved_amt=[]
comment=[]

next_customer_id=None
next_rebate_id=None

# load customer data file
def load_data_file(filename):
    try:
        with open(filename, 'r') as f:
            lines=f.readlines()
    except FileNotFoundError as e:
        print("Exception: %s" % e)
        sys.exit(1)

    for line in lines:
        if line.startswith('ID'):
            continue
        else:
            lock.acquire()
            id.append(line[:6])
            names.append(line[6:31].strip())
            emails.append(line[31:].strip())
            lock.release()
    #print(id,names,emails)

# load rebate processing data file
def load_rebate_file(filename):
    try:
        with open(filename, 'r') as f:
            lines=f.readlines()
    except FileNotFoundError as e:
        print("Exception:", e)
        sys.exit(1)

    lock.acquire()
    for line in lines:
        #skip first line
        if line.startswith('RebateID'):
            continue

        values=line.split(',')
        rebate_id.append(values[0])
        cust_id.append(values[1])
        purch_date.append(values[2])
        purch_amt.append(float(values[3]))
        submit_date.append(values[4])
        expect_rebate_amt.append(float(values[5]))
        approved.append(values[6])
        approve_date.append(values[7])
        if values[8] != "":
            approved_amt.append(float(values[8]))
        else:
            approved_amt.append(0.0)
        comment.append(values[9])
    lock.release()
    #print(rebate_id,cust_id,purch_date,purch_amt,submit_date,expect_rebate_amt,approved,approve_date,approved_amt,comment)

#validate email address
def check_email(email):
    if not email[0].isalnum():
        return False
    
    if '@' not in email:
        return False
    
    if not (email.endswith('.com') or email.endswith('.net') or email.endswith('.org')):
        return False
    
    return True

#Submit Rebate Information
def submit_rebate_info():
    #check until valid email address entered
    email_id=input("Enter email address: ")
    while not check_email(email_id):
        print("Invalid email address, please re-enter.")
        email_id=input("Enter email address: ")
    
    try:
        lock.acquire()
        #if new email id entered, create new customer
        if email_id not in emails:
            next_customer_id1=globals()['next_customer_id']
            id.append(next_customer_id1)
            name=input("Enter Fname and Lname separated by a comma: ")
            names.append(name.strip())
            emails.append(email_id)
            globals()['next_customer_id'] = next_customer_id1 + 1
        
        #if existing email id entered, update rebate information
        cust_id1=id[emails.index(email_id)]
        text=input("Enter purchase date, purchase amount and submission date separated by semicolons: ")
        next_rebate_id1=globals()['next_rebate_id']
        new_rebate_id='N'+str(next_rebate_id1)
        globals()['next_rebate_id'] = next_rebate_id1 + 1
        values=text.split(';')

        rebate_id.append(new_rebate_id)
        cust_id.append(cust_id1)
        purch_date.append(values[0])
        amount=float(values[1])
        rebate_amt=round(amount*12/100,2)
        purch_amt.append(amount)
        submit_date.append(values[2])
        expect_rebate_amt.append(rebate_amt)
        approved.append('')
        approve_date.append('')
        approved_amt.append(0.0)
        comment.append('')
    except Exception as e:
        print("Exception: %s" % e)
    finally:
        lock.release()

#Update Rebate Information
def update_rebate_info():
    text=input("Enter rebate update information: ")
    values=text.split('|')
    status=values[0]
    rebate_id1=values[1]
    approve_date1=values[2]

    try:
        lock.acquire()
        #throw error if rebate_id does not exist
        if rebate_id1 not in rebate_id:
            print("Error: Specific RebateID is not in Rebate Data")
            return
        
        #update rebate data based on approval status
        if status == 'Approve':
            id_index=rebate_id.index(rebate_id1)
            approved_amt1=expect_rebate_amt[id_index]
            approved1='Yes'
            comment1=""
        elif status == 'Partial':
            approved_amt1=float(values[3])
            approved1='Partial'
            comment1=values[4]
        elif status == 'Reject':
            approved_amt1=0
            comment1=values[3]    
            approved1='No'    

        index=rebate_id.index(rebate_id1)
        approved[index]=approved1
        approve_date[index]=approve_date1
        approved_amt[index]=approved_amt1
        comment[index]=comment1
    except Exception as e:
        print("Exception: %s" % e)
    finally:
        lock.release()

#get rebates count of a customer
def f_Count_RebateSubmissions( customernumber, rebatecustomeridlist ):
    return rebatecustomeridlist.count(customernumber)

#get rebates total amount of a customer
def f_Total_RebateSubmissions( customernumber, rebatecustomeridlist, rebateexpectedamountlist ):
    summ = 0
    for index,id in enumerate(rebatecustomeridlist):
        if id == customernumber:
            summ += rebateexpectedamountlist[index]
    return summ
    
#Generate Customer Rebate Report
def gen_customer_rebate_report():
    print("CUSTOMER REBATE SUMMARY REPORT")
    print("")

    try:
        lock.acquire()
        #loop for each customer id
        for i in range(len(id)):
            #check if customer has any rebate records
            if id[i] not in cust_id:
                continue

            #get customer rebate count and total rebate amount
            count=f_Count_RebateSubmissions(id[i], cust_id)
            amount=f_Total_RebateSubmissions(id[i], cust_id,expect_rebate_amt)

            #print customer information, rebate count, rebate amount
            print("")
            print(f"Rebate".rjust(73)+"Rebate".rjust(12))
            print(f"CustID".ljust(8)+"CustomerName".ljust(27)+"CustomerEmail".ljust(32)+" Count   "+"Amount".rjust(9))
            print("")
            print(str(id[i]).ljust(8)+names[i].ljust(27)+emails[i].ljust(32)+str(count).rjust(6)+"   $"+f"{amount:.2f}".rjust(8))
            print("")
            print(" "*68+"Approve".ljust(10))
            print(" "*13+"Purchase".center(22,"-")+" "*14+"Expected  Approve  "+"Reject".ljust(12)+"Rebate".center(10))
            print("   "+"RebateID"+"  "+"Date".ljust(12)+"Amount".rjust(10)+"  SubmitDate    Rebate   Reject  "+"Date".ljust(12)+"  Amount  Comment")

            #for customer each record in rebate cust_id list, print rebate information
            for id_index,cust_id1 in enumerate(cust_id):
                if cust_id1 != id[i]:
                    continue
                print("   "+rebate_id[id_index]+"  "+purch_date[id_index].ljust(10)+"  $ "+f"{purch_amt[id_index]:.2f}".rjust(8)+"  "+submit_date[id_index].ljust(10)+"  $"+f"{expect_rebate_amt[id_index]:.2f}".rjust(7)+"  "+approved[id_index].center(7)+"  "+approve_date[id_index].ljust(10)+"  $"+f"{approved_amt[id_index]:.2f}".rjust(7)+"  "+comment[id_index])

            print("_"*80)

    except Exception as e:
        print("Exception: ",e)
    finally:
        lock.release()

#Output Raw Customer List Information
def output_customer_list_info():
    try:
        lock.acquire()
        print(id)
        print("-"*10)
        print(names)
        print("-"*10)
        print(emails)
    except Exception as e:
        print("Exception: ",e)
    finally:
        lock.release()
    
#Output Raw Rebate List Information
def output_rebate_list_info():
    try:
        lock.acquire()
        print(rebate_id)
        print("-"*10)
        print(cust_id)
        print("-"*10)
        print(purch_date)
        print("-"*10)
        print(purch_amt)
        print("-"*10)
        print(submit_date)
        print("-"*10)
        print(expect_rebate_amt)
        print("-"*10)
        print(approved)
        print("-"*10)
        print(approve_date)
        print("-"*10)
        print(approved_amt)
        print("-"*10)
        print(comment)
    except Exception as e:
        print("Exception:",e)
    finally:
        lock.release()

# main codes starts here

#get customer file
customerfilename=input("Enter name of customer file to use: ")
thread1=threading.Thread(target=load_data_file,args=(customerfilename,))
thread1.start()


#get rebate processing file
rebatefilename=input("Enter name of rebate file to use: ")
thread2=threading.Thread(target=load_rebate_file,args=(rebatefilename,))
#load_rebate_file(rebatefilename)
thread2.start()


# Wait for both threads to finish
thread1.join()
thread2.join()

#get next customer id and rebate id
next_customer_id=GetNextCustomerID(customerfilename)
next_rebate_id=GetNextRebateID(rebatefilename)

if next_customer_id is None or next_rebate_id is None:
    sys.exit(1)

#menu processing
while True:
    option=Display_Menu()
    match option:
        case '1':
            #submit_rebate_info()
            thread=threading.Thread(target=submit_rebate_info)
            thread.start()
        case '2':
            #update_rebate_info()
            thread=threading.Thread(target=update_rebate_info)
            thread.start()
        case '3':
            #gen_customer_rebate_report()
            thread=threading.Thread(target=gen_customer_rebate_report)
            thread.start()
        case '4':
            #output_customer_list_info()
            thread=threading.Thread(target=output_customer_list_info)
            thread.start()
        case '5':
            #output_rebate_list_info()
            thread=threading.Thread(target=output_rebate_list_info)
            thread.start()
        case 'X' | 'x':
            sys.exit(0)
    # Wait for both threads to finish
    thread.join()