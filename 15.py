for a in range(10000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if ( ((x + 5 * y)<=200) or (y <= x+2) or (y + 9 >= a))==False:
                flag = False
                break
    if flag:
        print(a)
#wait until stop spawning new a. answer is 43
print('done')
