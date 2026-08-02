# list

# Python lists are mutable
l = [1, 'abc', True]
l2 = l.copy()
l2[0] = 2
# l2.extend([5, 12])
# l2 += [5, 12]
# print(l)
# print(l2)

# Copy on write
a = 'Hello'
b = a
b += ', world!'
# print(a)
# print(b)

# stack (LIFO: Last in first out)

# print(l2)
# print(l2.pop())
# print(l2)

# queue (FIFO: First in first out)

# q = []
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.pop(0))
# print(q)
# print(q.pop(0))
# print(q)
# print(q.pop(0))
# print(q)

# from collections import deque
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())



"""matrix"""

# l = [0] * 1000
# print(l)

# matrix = [[0] * 4] * 3
# print(matrix)
# matrix[0][1] = 1
# print(matrix)

# matrix = [[0 for col in range(4)] for row in range(3)]
# matrix[0][1] = 1
# print(matrix)


"""slicing"""


# [1,  2,  3,  5,  7,  9]
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

# l = [1, 2, 3, 5, 7, 9]
# s1 = l[::]
# l[0] = 6
# print(l)
# print(s1)


l = ['1', '123', '2']
l = list(map(int, l)) #cast int
uneven = list(filter(lambda x: x % 2 == 1, l)) #fard bashd
# uneven = [x for x in l if x % 2 == 1]
print(uneven)



# dict
# d = {
#     'Ali': '09123456789',
#     'Reza': '09123456782',
# }
# for key in d.keys():
#     print(key)
# for value in d.values():
#     print(value)
# for key, value in d.items():
#     print(key, value)

# if 'Ali' in d:
#     print('Yes')

# del d['Ali']
# print(d['Reza'])

# squares = {x: x * x for x in range(6)}
# print(squares)




# set
# s = {'a', 'e', 'i', 'o', 'u'}
# print(s)
# s.add('b')
# s.add('b')
# print(s)
# s.remove('b')
# print(s)
# s.pop()
# print(s)

# s1 = s
# s2 = {1, 2, 3, 4, 'a', 'b'}

# print(s1 | s2) # union
# print(s1 & s2) # intersection
# print(s1 - s2) # difference
# print(s1 ^ s2) # symmetric difference ((s1 | s2) - (s1 & s2))

# l = [1, 2, 3, 1, 2]
# s = set(l)
# print(s)

# l = [1, 2, 3]
# s = {l}
# print(s) # error


# priority queue (heap)
# from queue import PriorityQueue
# customers = PriorityQueue()
# customers.put((2, 'Harry'))
# customers.put((3, 'Charles'))
# customers.put((1, 'Riya'))
# customers.put((4, 'Stacy'))
# while customers:
#      print(customers.get())
