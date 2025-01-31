'''
E
DE
CDE
BCDE
ABCDE
'''

n = 5
for i in range(n):
    char = 69-i
    for j in range(i+1):
        print(chr(char + j), end="")
    print()

'''
i=0
    j=0
    chr(70)
'''

