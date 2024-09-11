
def transfer_money(from_bank, to_bank, amount):
    if amount <= 0:
        return "Invalid amount. Please enter a positive number."
    
    if from_bank.balance < amount:
        return "Insufficient funds in the source account."
    
    from_bank.balance -= amount
    to_bank.balance += amount
    
    return f"Successfully transferred ${amount} from {from_bank.name} to {to_bank.name}."

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# Example usage
bank1 = Bank("Bank One", 1000)
bank2 = Bank("Bank Two", 500)

print(f"{bank1.name} initial balance: ${bank1.balance}")
print(f"{bank2.name} initial balance: ${bank2.balance}")

transfer_amount = 300
result = transfer_money(bank1, bank2, transfer_amount)
print(result)

print(f"{bank1.name} final balance: ${bank1.balance}")
print(f"{bank2.name} final balance: ${bank2.balance}")
