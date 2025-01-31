'''
[stars, spaces]
[1,4]
[2,3]
[3,2]
[4,1]
[5,0]
[4,1]
[3,2]
[2,3]
[1,4]

*
**
***
****
*****
****
***
**
*
'''


n=5
for i in range(n+1):
    # Stars
    for j in range(i):
        print('*', end='')
    print()

for i in range(1,n):
    for j in range(n-i):
        print('*', end='')
    print()