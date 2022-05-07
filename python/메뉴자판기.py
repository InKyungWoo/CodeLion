import time
import random

lunch = ["된장찌개", "피자", "치킨"]

while True:               # 입력 기능
    print(lunch)
    item = input("메뉴를 입력해주세요 : ")
    if (item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)    # 중복 메뉴 제거, 차집합 연산하기 위해 집합화!
while True:               # 삭제 기능
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if (item == "q"):
        break
    else: 
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
                   
print("5")
time.sleep(1)

print("4")
time.sleep(1)

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("1")
time.sleep(1)

print(random.choice(list(set_lunch)))     # random.choice()는 리스트에서만 사용할 수 있음
