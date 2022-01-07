# 11. 함수만들기

#함수는 위쪽에 적어야함.
'''
def add(a,b):
    c = a+b
    print(c)

add(3,2)
add(5,7)

def add(a,b):
    c = a+b
    return c

print(add(3,2))
x = add(3,2)
print(x)

#함수는 여러개의 값을 리턴할 수 있다.(튜플 구조로 리턴함)
def add(a,b):
    c = a+b
    d = a-b
    return c,d
print(add(3,2))
'''
#소수만 출력하는 함수 만들기
def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

a = [12,13,7,9,19]
for x in a:
    if isPrime(x):
        print(x, end=' ')
print()