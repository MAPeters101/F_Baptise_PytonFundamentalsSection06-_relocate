message = "The definitive guide to Python"
print(message.upper())
print(message.lower())
print(message)
print(message.title())

print('abc' == 'ABC')
print('aBc'.lower() == 'AbC'.lower())

l = '\u03b1'
u = '\u0391'

print(l, u)
print(l == u)

print(l.lower() == u.lower())

a = '🐍'
print(a.lower() == a.upper())

print(l.casefold(), u.casefold(), l.casefold() == u.casefold())

street = 'stra\N{LATIN SMALL LETTER SHARP S}e'
print(street)
print(street.upper())
print(len(street), len(street.upper()))

data = 'STRASSE'
print(data == street)
print(data.lower(), data.lower() == street)
print(data.lower(), street)
print(data.casefold(), street.casefold())
print(data.casefold() == street.casefold())

s1 = '\N{LATIN SMALL LETTER E WITH CIRCUMFLEX}'
s2 = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print(s1, s2)
print(s1 == s2)
print(s1.upper() == s2.upper())
print(s1.casefold() == s2.casefold())

#  ========== Stripping ==========
name = 'Peter '
print(f'|{name}|')
print(f'|{name.rstrip(' ')}|')


name = '\t Peter\tJones\t '
print(f'|{name}|')
print(f'|{name.strip(' ')}|')
print(f'|{name.strip()}|')

name = 'ababPYTHONabab'
print(f'|{name}|')
print(f'|{name.strip(' ')}|')
print(f'|{name.strip('ab')}|')

print('Python' + ' ' + 'rocks' + '!')

data = 'Jones,Peter'
split_data = data.split(',')
print(split_data)

data = 'Jones,Peter,100'
split_data = data.split(',')
print(split_data)

data = 'Jones,Peter'
last_name, first_name = data.split(',')
print(first_name, last_name)

data = ['item 1', 'item 2', 'item 3']
print(', '.join(data))
print(','.join('ABCD'))

print('rock' in 'python rocks!')
print('Rock' in 'python rocks!')
print('Rock'.casefold() in 'python rocks!'.casefold())

print(1 in (1,2,3))
print('abc' in ('abc', 'def'))

print('Python rocks'.startswith('Python'))
print('Python rocks'.endswith('rocks'))
print('Python rocks'.casefold().endswith('rocks'.casefold()))

print('========== Substring ==========')
message = "To every action there is a always an equal and opposite reaction."
print(message.index('every'))
#print(message.index('Newton'))
print(message.find('Newton'))

print([1,2,3,4].index(2))
#print([1,2,3,4].find(2))
print(2 in [1,2,3,4])

print(message.index('action', 9 + len('action')))

from timeit import timeit

message = "Imagination is more important than knowledge - Einstein"

print(timeit("'Einstein' in message", globals=globals(), number=10_000_000))
print(timeit("message.find('Einstein')", globals=globals(), number=10_000_000))
print(timeit("message.index('Einstein')", globals=globals(), number=10_000_000))

