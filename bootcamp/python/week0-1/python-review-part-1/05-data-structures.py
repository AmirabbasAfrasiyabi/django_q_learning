# list

# Python lists are mutable
l = [1, 'abc', True]
l2 = l.copy()
l2[0] = 2
print(l2)
# l2.extend([5, 12])
# l2 += [5, 12]
# print(l)
# print(l2)


"""
create  algorithm  
for find the lowest value of in the list
"""

# my_array = [7,12,14,16,17,13,16]
# print(my_array)
# min_val = sorted(my_array)
# min_value = my_array[0]
# for i in my_array:
#     if i < min_value:
#         min_value = i
# print(min_value)



# Copy on write
a = 'Hello'
b = a
b += ', world!'
# print(a)
# print(b)



# stack (LIFO: Last in first out)

"""
pop (remove)
push (add)
peek (return to  last element on the stack)([-1])
isEmpty (check if the stack is empty)
"""

# stack=[]
#
# #push
# stack.append(-1)
# stack.append(0)
# stack.append('C')
# stack.append('H')
# stack.append('E')
#
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
# isEmpty = not bool(stack)
# print("isEmpty :" , isEmpty)



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
print("Queue : ", q)

"""peek"""
print("peek : " , q[0])


"""Dequeue"""
print(q.pop(0))
print(q)
print(q.pop(0))
print(q)
print(q.pop(0))
print(q)


"""isEmpty"""

isEmpty = not bool(q)
print("isEmpty: ", isEmpty)



# from collections import deque
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())


"""hash table with python"""

"""
1- Create an empty list (it can also be a dictionary or a set).
2- Create a hash function.
3- Inserting an element using a hash function.
4- Looking up an element using a hash function.
5- Handling collisions.
"""

# step 1 - create empty list

my_list = [None , None , None , None, None
    , None , None , None ,None , None ]

def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)

    return sum_of_char % 10

print("'bob' has hash code : ", hash_function('bob'))

def add(name):
  index = hash_function(name)
  my_list[index] = name

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)


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
