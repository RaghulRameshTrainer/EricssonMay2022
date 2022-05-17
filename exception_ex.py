'''
Exception has 4 clauses:
try
except
else
finally
'''
try:
    with open('customers.txt') as fo:
        print(fo.read())
    # num=int(input("Enter a number for reciprocate :"))
    # print(1/num)
    age = int(input("Enter your age:"))
    if age < 0  or age > 100:
        raise ValueError('Age should be between 0 to 100')
    age+=1
    print("You are {} years of old by 2023".format(age))

    import sqlite3

    dbh=sqlite3.connect("mydb.db")
    c=dbh.cursor()
    c.execute("SELECT * FROM customer")

except FileNotFoundError as e:
    print("The customers.txt file is missing.",e)
except PermissionError as e:
    print("Permission needs to be granted for reading customer.txt file")
except ZeroDivisionError as e:
    print("Can't divide by zero,",e)
except ValueError as e:
    print("AGE ERROR :",e)
except Exception as e:
    print("General Exception Executed. The error is :",e)

else:
    print("From else block that run when there is no exception")
finally:
    print("From finally clause that run all the times")
    print("Closing the database objects now:")
    c.close()
    dbh.close()