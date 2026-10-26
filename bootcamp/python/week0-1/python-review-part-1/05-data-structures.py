"""list"""
# Python lists are mutable
l = [6,
     2,
     10,
     3,
     5,]
# print(l)
# print(l[1])
# print(l[2])
# print(l[-1])
# print(l[-2])
# print(l[:-3])

"""not good syntax """
#print(l.sort) # -> none
#print(l.reverse) # -> none
# print(l.sort(reverse=True)) # -> none

"""good syntax """
#reverse
l.sort()
# print(l)
l.reverse()
# print(l)
# print(l.count(1))
l.sort(reverse=True)
# print(l)


#copy
"""incorrect"""
# l2 = l
# l2[0] = 2
# print(l2)
# print(l)

"""correct"""
l = [1,2,3,4,5,6,7,8,9]
l2 = l.copy()
l2[0] = 123
# print(l2)

# Copy on write
a = 'Hello'
# b = a
# b += ', world!'
# print(a)
# print(b)

l2.insert(1, 3)
# print(l2)
l.append([1,2,3])
# print(l)
l2.extend([5, 12])
# l2 += [5, 12]
# print(l)
# print(l2)


# stack (LIFO: Last in first out)
"""
pop (remove)
push (add)
peek (return to  last element on the stack)([-1])
isEmpty (check if the stack is empty)
"""

stack=[]

#push
stack.append(-1)
stack.append(0)
stack.append('C')
stack.append('H')
stack.append('E')

# print("stack : ", stack)
#
# # peek
# print("peek :" , stack[-1])
#
# #pop
#
# print("pop :" , stack.pop())
#
# #is empty
isEmpty = not bool(stack)
# print("isEmpty :" , isEmpty)


a = []
a.append(1)
a.append(2)
a.append(3)
# print(a)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)


# queue (FIFO: First in first out)
"""
Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.
"""


q = []
"""Enqueue"""
q.append(1)
q.append(2)
q.append(3)
# print("Queue : ", q)

"""peek"""
# print("peek : " , q[0])


"""Dequeue"""
# print(q.pop(0))
# print(q)
# print(q.pop(0))
# print(q)
# print(q.pop(0))
# print(q)


"""isEmpty"""

isEmpty = not bool(q)
# print("isEmpty: ", isEmpty)


from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())


"""matrix"""
l = [0]*100
# print(l)

matrix = [[0] * 4] * 3
# print(matrix)
matrix[2][2] = 45
# print(matrix)

matrix = [[0 for i in range(4)] for j in range(4)]
# print(matrix)
matrix[2][2] = 45
# print(matrix)


"""slicing"""
# [1,  2,  3,  5,  7,  9]
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

l = [1,
     2,
     3,
     5,
     7,
     9,
     ]

#print(i,j-1)

# print(l[:5])
# print(l[5:])
# print(l[5: 13])

"""copy"""
# s1 = l.copy()
s1 = l[::]

l[0] = 6
# print(l)
# print(s1)


l = ['1',
     '123',
     '2',]
l = list(map(int, l)) #cast int
uneven = list(filter(lambda x: x % 2 == 1, l)) #fard bashd
# uneven = [x for x in l if x % 2 == 1]
# print(uneven)


"""tuple"""
# print(i,j)
t = (10,
     4,
     5,
     1,
     )
# print(t[0])
# print(t[1])
# print(t[0:-1])
# print(t * 2)


"""swich"""
a, b, c = [1, 2, 3]
# print(a)
# print(b)
# print(c)

# print('---')
a, b, c = c, b, a  # 3-way swap in one statement!
# print(a)
# print(b)
# print(c)


"""dict"""
d = {
    'Ali': '09123456789',
    'Reza': '09123456782',
    'Amirabbas':'09120910309',
    'Atiye':'09120034660',
}

# print(d)
# print(len(d))
# print(d['Ali'])
# print(d['Reza'])

# print('-- add:')
d['Maman'] = '09120781057'
# print(d)

# for key in d.keys():
    # print(key)
# for value in d.values():
    # print(value)
# for key, value in d.items():
    # print(key, value)

# if 'Ali' in d:
    # print('Yes')

del d['Ali']
# print(d['Reza'])

"""set"""
s = {'a', 'e', 'i', 'o', 'u',1,2,1,3,2,1,3,1}


# print('--add--')
# s.add('b')
# s.add('b')
# print(s)
# print(b in s)
#
# print('remove')
# s.remove('b')
# print(s)
# s.pop()
# print(s)
# print(b in s)

s1 = s
s2 = {1, 2, 3, 4, 'a', 'b'}
#
# print(s1 | s2) # union
# print(s1 & s2) # intersection
# print(s1 - s2) # difference
# print(s1 ^ s2) # symmetric difference ((s1 | s2) - (s1 & s2))


"""
dict and list are not add in set 
because the the set member are Hashable
"""
# l = [1, 2, 3, 1, 2]
# s = set(l)
# print(s)

# l = [1, 2, 3]
# s = {l}
# print(s) # error


"""for - while"""

# print("----- example 1 ----")
# count = 5
# while count > 0:
#     print('continue' + str(count))
#     count -= 1

# print("----- example 2 ----")
# for i in range (2,10,3):
#     print(i)

# print("----- example 3 ----")
for key in d:  # you can iterate dictionaries too!
    print(key, ':', d[key])

# print('-----------')

print(list(d.items()))

for key, value in d.items():
    print(key, ':', value)



print("----- example 4 ----")
# a = [9135233333, 9123222233, 9212312121]
# b = ['iman', 'rasoul', 'fateme']
# for x, y in zip(a, b):
#     print(x, y)


"""heapq"""
# priority queue (heap)
# from queue import PriorityQueue
# customers = PriorityQueue()
# customers.put((2, 'Harry'))
# customers.put((3, 'Charles'))
# customers.put((1, 'Riya'))
# customers.put((4, 'Stacy'))
# while customers:
#      print(customers.get())
