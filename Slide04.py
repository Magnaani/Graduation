print("-" * 60)

import random

l = []
p = 0
i = 0

for x in range(10):
    l.append(random.randint(1, 100))
    if l[x] % 2 == 0:
        p += 1
    else:
        i += 1
print(f"Temos {p} números pares e {i} números ímpares.")

print("-" * 60)

print(l)
