try:
    print(10/0)
except ArithmeticError as e:
    print("Arithmetic error occurred:", e)



class InsufficientBalanceError(Exception):
    def __init__(self, field, message):
        self.message = message
        self.field = field
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("balance", "Insufficient balance to withdraw")
    
    return balance - amount



try: 
    withdraw(1000, 2000)
except ValueError as e:
    raise InsufficientBalanceError("balance", "Insufficient balance to withdraw", "insufficient_balance") from e