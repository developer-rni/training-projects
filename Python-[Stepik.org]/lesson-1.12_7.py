a = int(input())
b = int(a // 1000)
d = int(b // 10)
e = int(b % 10)
f = int(d % 10)
g = int(d // 10)
c = int(a % 1000)
h = int(c // 10)
j = int(c % 10)
k = int(h % 10)
l = int(h // 10)
summ1 = int(e + f + g)
summ2 = int(j + k + l)
if summ1 == summ2:
    print('Счастливый')
else:
    print('Обычный')
