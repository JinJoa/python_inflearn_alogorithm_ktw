# 6. 중첩반복문 (2중 for문)
'''
for i in range(5):
    print('i:',i, sep='',end=' ')
    for j in range(5):
        print('j:',j, sep='',end=' ')
    print()
'''

#별 삼각형
for i in range(5):
    for j in range(i+1):
        print("*",end=' ')
    print()


print("--------")

#별 역삼각형
for i in range(5):
    for j in range(5-i):
        print("*",end=' ')
    print()

