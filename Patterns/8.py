'''
[0,9,0]
[1,7,1]
[2,5,2]
[3,3,3]
[4,1,4]
'''

n=5
for i in range(n):
    # Space (i)
    for j in range(i):
        print(' ', end='')

    # Stars (2*(n-i)-1) 2*(5-0)-1 = 9
    for j in range(2*(n-i)-1):
        print('*', end='')
    
    # Space (i)
    for j in range(i):
        print(' ', end='')
    
    print()

'''
1st loop: i=0
*********
2nd loop: i=1
*********
 *******  
3rd loop: i=2
*********
 ******* 
  *****  
4th loop: i=3
*********
 ******* 
  ***** 
   ***
5th loop: i=4
*********
 ******* 
  ***** 
   ***
    *
'''