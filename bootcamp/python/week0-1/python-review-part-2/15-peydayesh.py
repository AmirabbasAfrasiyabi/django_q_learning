def find(num1, num2, num3):
    return list({1, 2, 3, 4} - {num1, num2, num3})[0]

print(find(1, 2, 4))
