accounts = {
    'savings':1500,
    'current':2000
}

def add_balance(amount: float, name: str) -> float:
    accounts[name] += amount
    return accounts[name]

transactions = [
    (10000, 'savings'),
    (150, 'current'),
    (-100, 'savings'),
    (150, 'current'),
    (100, 'savings'),
    (-150, 'current'),
    (-100, 'savings'),
    (150, 'current'),
]

for t in transactions:
    # add_balance(t[0], t[1])
    # add_balance(*t)  # arg unpacking
    add_balance(name=t[1], amount=t[0])  # named arg

print(accounts['savings'])
print(accounts['current'])

print("------another ex-------")
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# dict
users = [
    {'username':'Rolf', 'password':'123'},
    {'username':'Martin', 'password':'345'}
]

# users_objects = [ User(username=data['username'], password=data['password']) for data in users ]
# a better way of doing it to avoid dup username username password password is
users_objects = [ User(**data) for data in users ] # named dict unpacking

print(users_objects[0].username)
print(users_objects[0].password)
print(users_objects[1].username)
print(users_objects[1].password)

# tuple
users = [
    ('rolf', '123456'),
    ('mary','000')
]
users_objects = [ User(*data) for data in users ] # named tuple unpacking
print(users_objects[0].username)
print(users_objects[0].password)