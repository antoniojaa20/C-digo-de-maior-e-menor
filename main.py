import math
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
Mab = (a +b+ abs(a-b))/2
Mabc = (Mab + c + abs(Mab-c))/2
print('%.0f eh o maior'%Mabc)