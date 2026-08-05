n, q, l = map(int, input().split())

d = {}
for i in range(n):
    key, value = input().split()
    d[key] = value
for i in range(q):
    key = input()
    print(d[key] if key in d else 'Unknown')
