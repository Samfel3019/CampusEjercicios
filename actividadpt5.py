s = 3
n = 6
for i in range (1, 6+s):
    if i <= 2:
        n1= 1
        n2 = 1
    else:
        if i % 2 != 0:
            v= n1 + n2
else:
    v = n1 - n2
    n1 = n2
    n2 = v