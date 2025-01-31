# combining patterns
'''
[4,1,4]
[3,3,3]
[2,5,2]
[1,7,1]
[0,9,0]
[0,9,0]
[1,7,1]
[2,5,2]
[3,3,3]
[4,1,4]

    *    
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''


def upper_pattern(n):
    for i in range(1,n+1):
        # Space
        for j in range(n-i):
            print(' ', end='')
        
        # Star 2*i-1
        for j in range(2*i-1):
            print('*', end='')
        
        # Space
        for j in range(n-i):
            print(' ', end='')
    
        print()
        
def lower_pattern(n):
    for i in range(n):
        # Space
        for j in range(i):
            print(' ', end='')
        
        # Star
        for j in range(2*(n-i)-1):
            print('*', end='')
            
        # Space
        for j in range(i):
            print(' ', end='')
        print()
    
upper_pattern(5)
lower_pattern(5)