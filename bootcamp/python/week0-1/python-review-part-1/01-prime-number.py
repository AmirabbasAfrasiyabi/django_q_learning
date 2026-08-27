from math import sqrt

# Check if a number is prime
# O(n)
# O(sqrt(n))
# Omega(1)

"""solution 1 -> way 1"""
# def is_prime(n):
#     if n < 2:
#         return False
#     is_prime = True
#     for i in range(2, n ):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("n is prime")
#     else:
#         print("n is not prime")
# is_prime(13)

"""solution1 -> way 2"""
# n = int(input("Enter a number: "))
# is_prime = True
# for i in range(2,n):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("n is prime")
# else:
#     print("n is not prime")
# print(is_prime)


"""solution2 -> way 1"""
# def is_prime(n):
#     if n < 2:
#         return False
#     is_prime = True

    # for i in range(2, n//2 ): #-> error

        # error
        # 4 is not prime
        # 2 is prime
        # 4 //2 == 2

#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("n is prime")
#     else:
#         print("n is not prime")
# is_prime(4)

"""solution2 -> way 2"""
# n = int(input())
# isPrime = True
# for i in range(1, n//2 +1):
#     if n % i == 0:
#         isPrime = False
# if isPrime:
#     print('n is prime')
# else:
#     print('n is not prime')


"""solution3 -> way 1"""
# def is_prime(n):
#     if n < 2:
#         return False
#     is_prime = True
#
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("n is prime")
#     else:
#         print("n is not prime")
# is_prime(4)

"""solution3 -> way 2"""
# n = int(input())
# isPrime = True
# for i in range(2, int(sqrt(n)) + 1):
#     if n % i == 0:
#         isPrime = False
# if isPrime:
#     print('n is prime')
# else:
#     print('n is not prime')