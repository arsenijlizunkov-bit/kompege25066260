with open("24_18562.txt") as f:
    a = f.readline()

rez = []
start = 0
end = 1
while end <= len(a):
    s = a[start:end]
    if 'XYYYZ' in s:
        rez.append(len(s))
        start = end-3
    end +=1
print(max(rez))
#2042


