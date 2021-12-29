# 2. 변수입력과 연산
'''
a = input("숫자를 입력하세요 : ")
print(a)
print(type(a))

a, b = input("숫자를 입력하세요 : ").split()
print(type(a))
c = a+b
print(type(c))

a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(a+b)

a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)

#사칙연신
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
'''

#실수랑 정수랑 더하면 무슨 타입?
a=4.3
b=5
c=a+b
print(type(c))
