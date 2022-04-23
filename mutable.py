friends_last_seen = {
    'Rolf' : 0,
    'Jose' : 1,
    'Mary' : 2
}

print(id(friends_last_seen))

another = friends_last_seen
print(id(another))

another['Sri'] = 3  # whats happening is friends_last_seen.__setitem__(self, 'Sri')
print(id(another))
print(another)

print(id(friends_last_seen))
print(friends_last_seen)


my_int = 5
print(id(my_int))
my_int = 8
print(id(my_int))