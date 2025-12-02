def to9(n):
    s = ''
    while True:
        q = n%9
        s = str(q) + s
        n = n//9
        if n == 0:
            return s

#print('ok')
#for i in range(20):
#    print(to9(i))

def a(n):
    x = to9(n)
    if n%3 == 0:
        x = '2' + x[:-1] + '88'
    else:
        x = x + '01'
    return int(x, 9)

#print(a(4), a(12))
rez = []
for n in range(1, 100000, 2):
    r = a(n)
    if r > 65536:
        rez.append(r)
print(min(rez))

