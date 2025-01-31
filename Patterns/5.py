'''
****
***
**
*
'''



n=5

for i in range(1,n):
    for j in range(1,n-i+1):
        print('*', end='')
    print()

# 1st loop: n-i+1 = 5-1+1 = 5
# ****
# 2nd loop: n-i+1 = 5-2+1 = 4
# ****
# ***
# 3rd loop: n-i+1 = 5-3+1 = 3
# ****
# ***
# **
# 4th loop: n-i+1 = 5-4+1 = 2
# ****
# ***
# **
# *
# 5th loop: n-i+1 = 5-5+1 = 1
# ****
# ***
# **
# *