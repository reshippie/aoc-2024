#! /bin/env python

lines = []
with open('input.txt', encoding='utf-8') as f:
    lines = f.read().split('\n')
a = []
b = []
for l in lines:
    try:
        (c, d) = l.split()
        a.append(int(c))
        b.append(int(d))
    except ValueError as e:
        pass
a.sort()
b.sort()
total = 0
for i in range(len(a)):
    total += abs(a[i] - b[i])
print(total)
