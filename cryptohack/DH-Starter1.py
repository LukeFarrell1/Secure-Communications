p = 991
g = 209

#g * d %(mod) 991 = 1

for i in range (p):
    if (g*i) % 991 == 1 :
        print (i)
        break 