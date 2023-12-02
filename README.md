# customer_rebate_program

1. Main program: customer_rebate.py
2. functions file: CSE102P3_Functions.py 
3. sample input files:
   - data_file.csv ( customer info file )
   - rebate_file.csv ( rebate info file )

**Testing:**

Enter name of customer file to use:data_file.csv
['103256', '232653', '231123'] ['Briggs, Dan', 'Carter, Cinnamon', 'Collier, Barney'] ['briggsd@imf.org', 'carter@hartfordrepertory.org', 'barney@collierelectronics.com']
Enter name of rebate file to use:rebate_file.csv
['S7224418', 'Z5407587', 'I5262044', 'X6228975'] ['896429', '891087', '597409', '708247'] ['1/31/2023', '3/16/2023', '6/24/2023', '9/2/2023'] [616.89, 103.84, 182.25, 174.8] ['3/24/2023', '6/3/2023', '7/1/2023', '9/15/2023'] [74.03, 12.46, 21.87, 20.98] ['', 'No', 'Partial', 'Yes'] ['', '6/24/2023', '7/28/2023', '10/7/2023'] [0.0, 0.0, 13.95, 20.98] ['', 'Rebate request was submitted after 30 days', 'Items returned are not eligible for rebate', '']

------------------------
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program
------------------------
Enter Menu Option: 1
Enter email address: briggsd@imf.org
Enter purchase date, purchase amount and submission date separated by semicolons: 4/12/2023;123;4/13/2023

------------------------ 
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program 
------------------------
Enter Menu Option: 2
Enter rebate update information: Approve|N6228976|4/15/2023

------------------------ 
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program 
------------------------
Enter Menu Option: 3
CUSTOMER REBATE SUMMARY REPORT


                                                                   Rebate      Rebate
CustID  CustomerName               CustomerEmail                    Count      Amount

103256  Briggs, Dan                briggsd@imf.org                      1  $   14.76

                                                                    Approve
             -------Purchase-------              Expected  Approve  Reject        Rebate
   RebateID  Date            Amount  SubmitDate    Rebate   Reject  Date          Amount  Comment
   N6228976  4/12/2023   $   123.00  4/13/2023   $  14.76    Yes    4/15/2023   $  14.76
________________________________________________________________________________

------------------------
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program
------------------------
Enter Menu Option: 4
['103256', '232653', '231123']
----------
['Briggs, Dan', 'Carter, Cinnamon', 'Collier, Barney']
----------
['briggsd@imf.org', 'carter@hartfordrepertory.org', 'barney@collierelectronics.com']

------------------------
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program
------------------------
Enter Menu Option: 5
['S7224418', 'Z5407587', 'I5262044', 'X6228975', 'N6228976']
----------
['896429', '891087', '597409', '708247', '103256']
----------
['1/31/2023', '3/16/2023', '6/24/2023', '9/2/2023', '4/12/2023']
----------
[616.89, 103.84, 182.25, 174.8, 123.0]
----------
['3/24/2023', '6/3/2023', '7/1/2023', '9/15/2023', '4/13/2023']
----------
[74.03, 12.46, 21.87, 20.98, 14.76]
----------
['', 'No', 'Partial', 'Yes', 'Yes']
----------
['', '6/24/2023', '7/28/2023', '10/7/2023', '4/15/2023']
----------
[0.0, 0.0, 13.95, 20.98, 14.76]
----------
['', 'Rebate request was submitted after 30 days', 'Items returned are not eligible for rebate', '', '']

------------------------
1. Submit Rebate Information
2. Update Rebate Information
3. Generate Customer Rebate Report
4. Output Customer List Information
5. Output Rebate List Information
X. Exit Program
------------------------
Enter Menu Option: X
