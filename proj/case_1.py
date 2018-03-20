DEFAULT_X = -1
x = []

for i in range(30):
    print(i)
    x.append(i if i % 2 == 0 else DEFAULT_X)

print("Result:")
print(", ".join(map(str, x)))
