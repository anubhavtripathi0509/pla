'[Space, Stars, Space]'

'''
   *           [3, 1, 3]
  ***          [2, 3, 2]
 *****         [1, 5, 1]
*******        [0, 7, 0]

'''

n=4
for i in range(1,n+1):
    # Space (n-i) 4-1 = 3
    for j in range(n-i):
        print(' ', end='')
    
    # Stars (2*i-1) 2*1-1 = 1
    for j in range(2*i-1):
        print('*', end='')

    # Space (n-i) 4-1 = 3
    for j in range(n-i):
        print(' ', end='')

    print()