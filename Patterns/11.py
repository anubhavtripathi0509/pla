'''
1
01
101
0101
10101
'''

n=5
for i in range(1,n+1):
    if i % 2 == 0:
        start = 0
    else:
        start= 1

    for j in range(i):
        print(start, end='')
        start = 1-start
    print()