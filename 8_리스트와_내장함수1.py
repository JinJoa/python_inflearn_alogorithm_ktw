# 8. 리스트와 내장함수(1)

import random as r

#빈 리스트 만들기
a=[]
#print(a)
b=list()
#print(b)

#리스트 초기화하기
a = [1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c = a+b
#print(c)

#리스트 추가, 삽입, 삭제(pop, remove), 인덱스
print(a)
a.append(6)
print(a)

a.insert(3,7)
print(a)

a.pop()
print(a)
a.pop(3)
print(a)

a.remove(4)
print(a)

print(a.index(5))

#1~10을 가진 리스트 선언
a = list(range(1,11))
print(a)

#리스트의 합, 최대값, 최소값 구하기
print(sum(a))
print(max(a))
print(min(a))
print(min(7,5))
print(min(7,5,3))
print(a)
#리스트 셔플
r.shuffle(a)
print(a)
#리스트 내림차순 정렬
a.sort(reverse=True)
print(a)
#리스트 오름차순 정렬
a.sort()
print(a)
#리스트 비우기
a.clear()
print(a)