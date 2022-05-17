#import sys
from sys import *

if len(argv) != 3:
    print("Usage:{} {} {}".format(argv[0],'<customer_name>','<account_number>'))
    print("Please rerun with name and acct number.")
    exit(1)

print("Program Name:",argv[0]) 
print("Customer Name:",argv[1])
print("Account Number:",argv[2])
