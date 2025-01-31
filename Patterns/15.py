'''
ABCDE
ABCD
ABC
AB
A
'''

n = 5
for i in range(n+1):
    for j in range(n-i):
        print(chr(65+j), end='')
    print()