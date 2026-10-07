k = [1,2,[3,4]]
m = k.copy()
k[2].append(40)
print(m)
print(k)
k.append(35)
print(k)