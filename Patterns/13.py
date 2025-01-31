'''
1
23
456
78910
1112131415
'''


n=5
count=1
for i in range(n+1):
    for j in range(i):
        print(count, end='')
        count=count+1
    print()