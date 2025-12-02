def tri(n):
    n = int(n, 36)
    s = ''
    while n != 0:
        s = str(n%3) + s
        n = n//3
    return s

a = int("AAAB5", 23)
alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rez = -1303
for x in alp:
    s =  int(f'9AH{x}P', 36) + int('AAAB5', 23) -  int(f'LOL{x}', 36)
    if s%76 == 0:
        print(tri(x))


#122
