'''
기본 구문 - for + if
'''

scope = [1, 2, 3, 4, 5] # list
for x in scope:
    print(x)
    if x < 3:
        continue
    else:   
        break