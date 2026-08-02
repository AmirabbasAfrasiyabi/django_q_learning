# https://www.scaler.com/topics/caesar-cipher-python/
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# ASCII
# Unicode
# chr
# ord

# 97: a
# 65: A
# 97-122 -> 0-25
# Python strings are immutable
# Python lists are mutable
s = list(input())
is_decrypt = True if input() == '1' else False
# is_decrypt = (input() == '1') ? true : false
n = int(input()) % 26
if is_decrypt:
    n = 26 - n
for i in range(len(s)):
    s[i] = chr(((ord(s[i]) - 97 + n) % 26) + 97)
print(''.join(s))

# a % b
