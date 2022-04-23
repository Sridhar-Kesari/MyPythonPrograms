"""
counter
defaultdict - never raised key error
ordereddict
namedtuple
deque
"""

from collections import Counter, defaultdict, OrderedDict, deque
# counter
device_temp = [13.5, 14.1, 14.1, 14.1, 14.5, 14]
temperature_counter = Counter(device_temp)
print(temperature_counter[14.1])

# without defaultdict
coworkers = [('Rolf', 'MIT'), ('Jen', 'SIT'), ('George', 'KIT'), ('Rolf', 'MSRIT')]
almaters = {}
for coworker, place in coworkers:
    if coworker not in almaters:
        almaters[coworker] = []
    almaters[coworker].append(place)
print(almaters)

# defaultdict
almaters_new = defaultdict(list)
for coworker, place in coworkers:
    almaters_new[coworker].append(place)
almaters_new.default_factory = None
print(almaters['Rolf'])
print(almaters['Jen'])
# print(almaters['Ro'])

# another ex

my_comp = 'smartans'
coworkers = ['SK','DK','GK']
others = [('Rolf','Apple'),('Anna','Google')]
coworker_comp = defaultdict(lambda: my_comp)
for p, c in others:
    coworker_comp[p] = c
print(coworker_comp['SK'])
print(coworker_comp[coworker[0]])
print(coworker_comp[others[0][0]])

print("----------OrderedDic----------")
o = OrderedDict()
o['Rolf'] = 1
o['SK'] = 2
o['MK'] = 3
print(o)
o.move_to_end('Rolf')
print(o)
o.move_to_end('MK', last=False)
print(o)
o.popitem()
print(o)

print("==========deque==============")
friends = deque(('Rolf', 'SK', 'KL', 'HN'))
friends.append('RR')
friends.appendleft('Ant')
friends.pop()
friends.popleft()
print(friends)