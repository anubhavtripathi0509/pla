'''
[3, 1, 0, 3]
[2, 2, 1, 2]
[1, 3, 2, 1]
[0, 4, 3, 0]

   A   
  ABC
 ABCBA
ABCDCBA
'''

n = 4
for i in range(n):
    # Spaces
    for j in range(n-i-1):
        print(' ', end='')
    
    # Alpha half
    for j in range(i+1):
        print(chr(65+j), end='')

    # Alpha 2nd half
    for j in range(i):
        print(chr(65+i-j-1), end='')

    # Spaces
    for j in range(n-i-1):
        print(' ', end='')
    print()
