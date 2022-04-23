import re
email = 'sridhar.smartans@gmail.com'

expression = '[a-z]+'  # match characters - many times
matches = re.findall(expression, email)
print(matches)
name = f'{matches[0]}.{matches[1]}'
domain = f'{matches[2]}.{matches[3]}'
print(name)
print(domain)


expression = '[a-z\.]+' # match characters or a dot - many times
matches = re.findall(expression, email)
print(matches)
name = matches[0]
domain = matches[1]
print(name)
print(domain)

# with slpit

parts = email.split('@')
print(parts)
print(parts[0], parts[1])

print("--------")

price = 'Price: $123.50'
expression = '123.50'
matches = re.search(expression, price)
print(matches.group(0))
# print(matches.group(1))
expression = 'Price: \$123.50'
matches = re.search(expression, price)
print(matches.group(0))
#print(matches.group(1))
#--------------
expression = 'Price: \$(123.50)'
matches = re.search(expression, price)
print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets
#--------------
expression = 'Price: \$([0-9]*\.[0-9]*)'
matches = re.search(expression, price)
print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets
price_num = float(matches.group(1))
print(price_num)
#--------------
price = 'Price: $12,3456.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)' # 12,345.50
matches = re.search(expression, price)
print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets
price_without_comma = matches.group(1).replace(',', '')
price_num = float(price_without_comma)
print(price_num)