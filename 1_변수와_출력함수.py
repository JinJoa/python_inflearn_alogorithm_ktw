# 1. 변수와 출력함수
a=1
A=2
A1=3
print(a,A,A1)
a,b,c, = 3,2,1
print(a,b,c)

#값 교환
a, b = 10,20
print(a, b)
a, b = b, a

#변수 타입
a = 123456789123456789123456789
print(a)
print(type(a))
a = 12.123456789123456789123456789
print(a)
print(type(a))
a="student"
print(a)
print(type(a))

#출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a,b,c, sep=", ")
print(a,b,c, sep="")
print(a,b,c, sep="\n")
