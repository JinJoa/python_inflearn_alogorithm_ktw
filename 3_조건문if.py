# 3. 조건문 if (분기, 중첩)
'''
x = 7
if x ==7:
    print("Lucky")
    
x = 15
if x>=10:
    if x%2==1:
        print("10이상의 홀수")

x = 9
if x>0:
    if x<10:
        print("10보다 작은 자연수")
        
# and 사용 
x = 7
if x>0 and x<10:
        print("10보다 작은 자연수")

# 양수 음수 구별
x = 10
if x>0:
    print("양수")
else:
    print("음수")
'''
#성적 elif 사용
x = 93
if x>=90:
    print("A")
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print("F")


