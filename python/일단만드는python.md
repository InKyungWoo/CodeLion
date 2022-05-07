# 일단 만드는 Python

> 마트료시카 🪆

## Python으로 만드는 메뉴 자판기 

<details> 
  <summary>list & dictionary</summary>
  
```python
information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
print(information.get("취미"))    # -> 영화관람
information["특기"] = "피아노"      # "특기":"피아노" 추가
information["사는곳"] = "서울"      # "사는곳":"서울" 추가
del information["좋아하는 음식"]    # 좋아하는 음식:국수 -> 삭제
print(information)
print(len(information))         # 요소 개수
information.clear()              # 전체 삭제
print(information)
  
foods = ["된장찌개", "피자", "제육볶음"]  
print(foods[-2])    # -> 피자
foods.append("김밥") # 해당 요소 추가
del foods[1]        # 피자 삭제
print(foods)
  ```
  </details>
  
<details>
<summary>끝까지 반복하기</summary>
  
```python
foods = ["된장찌개", "피자", "제육볶음"]
  
for x in range(3):
    print(foods[x])
  
for x in foods:       # 이렇게 짜면 범위 지정할 필요 없음
    print(x)

information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x, y in information.items():
    print(x)        # -> 고향, 취미, 좋아하는 음식
    print(y)        # -> 수원, 영화관람, 국수
  ```
</details>

<details>
  <summary>집합 알아보기</summary>
  
 - 집합은 `중복` `순서` 없음!!
 - 출력시 순서 랜덤
 - `합집합` `차집합` `교집합`
  
 ```python
foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods)                         # foods 리스트를 집합으로 선언
foods_set2 = set(["된장찌개", "피자", "제육볶음"])    # 직접 바로 집합 만들기
print(foods_set1)
print(foods_set2)
 ```
</details>

<details>
  <summary>집합 사용하기</summary>
  
  ```python
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2         # 합집합
menu4 = menu1 & menu2         # 교집합
menu5 = menu1 - menu2         # 차집합
print(menu3)
  ```
</details>

<details>
  <summary>만약에</summary>
  
  ```python
  import random

  food = random.choice(["된장찌개","피자","제육볶음"])

  print(food)
  if(food == "제육볶음"):
      print("곱배기 주세요")
  else:
      print("그냥 주세요")
  print("종료")
  ```
</details>

<details>
  <summary>오늘은 뭐드실? <제작하기></summary>
  
  ```python
  lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

  while True:
      print(lunch)
      item = input("음식을 추가 해주세요 : ")
      if(item == "q"):
          break
      else:
          lunch.append(item)

  print(lunch)
  set_lunch = set(lunch)    # lunch 집합화
  ```
  
  ```python
  set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
  food = "짜장면"
  set_dinner = set_dinner - set([food])   # 집합 연산은 집합끼리만 가능. []리스트와, set() 집합화
  print(set_dinner)
  ```
</details>


<details>
  <summary>오늘은 뭐드실? <정리하기></summary>
  
  ```python
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
  ```
</details>

## Python으로 만드는 익명 질문 게시판

<details>
  <summary>함수 알아보기</summary>
  
  ```python
def make_dolcelatte():
    print("1. 얼음을 넣는다.")
    print("2. 연유를 30ml 넣는다.")
    print("3. 찬 우유를 넣는다.")
    print("4. 에스프레소샷을 넣는다.")

def make_blueberry_smoothie():
    print("1. 블루베리 20g을 넣는다.")
    print("2. 우유 300ml를 넣는다.")
    print("3. 얼음을 넣는다.")
    print("4. 믹서기에 간다.")

def make_simple_latte():
    print("1. 커피를 넣는다.")
    print("2. 우유를 넣는다.")
    print("3. 신나게 섞는다.")
 
make_dolcelatte()
```  
  </details>
  
<details>
  <summary>이상형이 뭐에요? <제작하기></summary><br>
    
- `{key:value}` <br>
  
1. dictionary 형태로 저장하기    
  
```python  
total_dictionary = {}     # 빈 dictionary 생성

while True:
  question = input("질문을 입력해주세요 : ")
  if question == "q"
    break
  else:
    total_dictionary[question] = ""

for i in total_dictionary: 
  print(i)
  answer = input("답변을 입력해주세요 : ")
  total_dictionary[i] = answer     # 해당 질문(key)에 대한 답변(value)을 i 위치에 저장

print(total_dictionary)
```

2. list 형태로 저장하기
```python
total_list = []     # 빈 리스트 생성

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)
```
  

</details>
  


