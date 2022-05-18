from bank import Account

acc=Account('Rajesh','ALNPR7121F',10000)
print("Balance:",acc.__balance)
print("Online Banking Details:")
print("=========================")
print("Username:",acc.user)
print("Password:",acc.password)

acc.__balance=1000000
print("Balance:",acc.__balance)
