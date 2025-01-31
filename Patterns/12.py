'''
[1, 3, 3, 1]
[2, 2, 2, 2]
[3, 1, 1, 3]
[4, 0, 0, 4]

1      1
12    21
123  321
12344321
'''

n=4
for i in range(1, n+1):
    # num
    for j in range(1,i+1):
        print(j, end='')
    
    # space
    for j in range(n-i):
        print(' ', end='')

    # space
    for j in range(n-i):
        print(' ', end='')

    # num
    for j in range(i, 0, -1):
        print(j, end='')

    print()