n = int(input())

temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")
