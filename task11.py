s = int(input())

if s < 100:
    l = 3000 - 125*(s**2)
    print(l)
else:
    l = 12000/(4+(s*s)/14900)
    print(l)
