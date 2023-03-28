a = [7, 10, 23, -19, 80]
a.sort()
print(a)
a.extend([20, 21])
print(a)
b = sorted(a)
print(b)
a = a[1::2]
print(a)
a = [-19, 7, 10, 20, 21, 23, 80]
print(a.count(20))
item = 20
index = a.index(item)
print(index)
a = [-19, 7, 10, 20, 21, 23, 80]
a[3] = 19
print(a)

