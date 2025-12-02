def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a+6, b)

print(f(12, 19) * f(19, 45))
# 966


