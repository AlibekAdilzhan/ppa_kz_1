n = 5
i = 0

s = -1
while i < n:
    x = int(input())
    if x > s:
        s = x
    i = i + 1

print("HIGHEST TREE", s)