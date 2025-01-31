'''
A
BB
CCC
DDDD
EEEEE
'''

n=5
for i in range(n):
    for j in range(i+1):
        print(chr(65+i), end='')
    print()

'''
0 - 5
    i=0
    (0 - 1)  A
    i=1
    (0 - 2) BB
    i=3
    (0 - 3) CCC
    i=4
    (0 - 4) DDDD
    i=5
    (0 - 5) EEEEE
'''