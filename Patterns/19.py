'''
[5, 0, 5]
[4, 2, 4]
[3, 4, 3]
[2, 6, 2]
[1, 8, 1]

[1, 8, 1]
[2, 6, 2]
[3, 4, 3]
[4, 2, 4]
[5, 0, 5]

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

n=5
def upper_half(n):
    for i in range(1,n+1):
        # Star
        for j in range(n-i+1):
            print('*', end='')
        
        # Space
        for j  in range(2*(i-1)):
            print(' ', end='')
        
        # Star
        for j in range(n-i+1):
            print('*', end='')

        print()

def lower_half(n):
    for i in range(1,n+1):
        # Star
        for j in range(i):
            print('*', end='')
        
        # Space
        for j in range(2*(n-i)):
            print(' ', end='')
        
        # Star
        for j in range(i):
            print('*', end='')
        
        print()

'''
i=1
10**
i=2
'''

upper_half(n)
lower_half(n)