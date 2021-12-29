# 4. 반복문(for, while)
'''
a = range(10)
print(list(a))

#1~10인 정수 리스트를 만드는 함수 
a = range(1,11)
print(list(a))

# hello 10번 출력
for i in range(10):
    print("hello")

#while문 사용 1에서 10까지 출력

i = 1
while i <=10:
    print(i)
    i = i+1

#10에서 1까지 출력
i = 10
while i >=1:
    print(i)
    i = i-1
    
#무한반복
i=1
while True:
    print(i)
    i+=1

#break. 반복문 멈추
i=1
while True:
    print(i)
    if i == 5:
        break
    i+=1

#continue. 건너뛰기 
for i in range(1, 11):
    if i%2==0:
        continue
    print(i)
'''

# for ~ else 구문 : for문 정상종료 시 else문 실행, break로 종료시 else문 실행안됨
#break로 종료되는 경우
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)

#정상종료되는 경우
for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)
