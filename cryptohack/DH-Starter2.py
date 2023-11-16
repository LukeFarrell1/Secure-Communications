# function = g^n % p | pow (g,n,p)

p = 28151
g = 2
found = False

while not found:
    for i in range (2,p):
        if pow(g,i,p) == 1:
            break
        if i == p -2:
            print(g)
            found = True
    g = g + 1