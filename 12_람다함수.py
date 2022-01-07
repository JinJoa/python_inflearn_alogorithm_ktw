# 12. 람다함수
'''
def plus_one(x):
    return x+1
print(plus_one(1))

# 람다함수 예시
pluse_two = lambda x: x+2
print(pluse_two(1))

'''

def plus_one(x):
    return x+1
a = [1,2,3]
print(list(map(plus_one, a)))

# 람다함수가 유용하게 사용될때
print(list(map(lambda x: x+1, a)))
