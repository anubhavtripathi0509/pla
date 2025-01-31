'''
1234
123
12
1
'''

n=5
for i in range(1,n):
    for j in range(1, n-i+1):
        print(j, end='')
    print()