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