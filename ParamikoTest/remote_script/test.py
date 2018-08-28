f = open('test.txt', 'w')

for x in xrange(1024 * 1024 * 4):
    if x % 1024 == 0:
        f.write('0')
    else:
        f.write('x')

f.close()




