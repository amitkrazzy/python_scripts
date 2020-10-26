x = {1: 2, 3: 9, 4: 3, 2: 1, 0: 0}
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})


print(x.items())

print({k:v for k,v in sorted(x.items(), key=(lambda item:item[1]))})
