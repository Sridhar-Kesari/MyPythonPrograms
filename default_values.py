accounts = {
    'savings':1500,
    'current':2000
}

def account_balance(amount: float, name: str = 'savings') -> float:
    accounts[name] += amount
    return accounts[name]

result = account_balance(100.5, 'current')
print(result)
print(accounts['savings'])
print(accounts['current'])
