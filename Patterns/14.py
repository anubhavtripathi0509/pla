'''
A
AB
ABC
ABCD
ABCDE
ABCD
ABC
AB
A
'''

n = 5
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j), end='')
    print()

for i in range(1,n):
    for j in range(n-i):
        print(chr(65+j), end='')
    print()