class BalanceException(Exception):
    pass

def checkBalance():
    principal = 15000
    withdraw = 14000
    try:
        balance = principal - withdraw
        if(balance<=2000):
            raise BalanceException("Insufficent Balance")
        print("Your Balance is :", balance)
    except BalanceException as be:
        print(be)

checkBalance()
