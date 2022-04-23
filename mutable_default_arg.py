# def create_account(name: str, holder: str, account_holders: list = []):
def create_account(name: str, holder: str, account_holders):
    account_holders.append(holder)

    return {
        'name' : name,
        'main_account_holder' : holder,
        'account_holders' : account_holders
    }


a1 = create_account('RD', 'Rolf', [])
a2 = create_account('SB', 'Mary', [])

print(a1)
print(a2)