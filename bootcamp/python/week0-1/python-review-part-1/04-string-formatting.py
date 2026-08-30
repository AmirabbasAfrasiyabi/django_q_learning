# Source: Python Tricks Book
# Recommended Book: CPython Internals

"""
    Old Style String Formatting
"""

name = 'Bob'
# print('Hello, %s' % name)

errno = 50159747054
# print('%x' % errno)

# print('Hey %s, there is a 0x%x error!' % (name, errno))


"""
    New Style String Formatting
"""

# 'Hello, {}'.format(name)

# 'Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)

"""
    Literal String Interpolation or f-strings (Python 3.6+)
"""

# print(f'Hello, {name}!')

a = 5
b = 10
# print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

# print(f'Hey {name}, there is a {errno:#x} error!')


