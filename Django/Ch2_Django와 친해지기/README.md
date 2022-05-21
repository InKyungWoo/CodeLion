# Chapter 2. Django와 친해지기

- 웹 프레임워크 : 웹서비스를 `쉽게` 만들어주는 기계
- Django : 상상한 내용을 웹으로 구현, 사용법이 `정형화` 되어있음

<details>
  <summary>Python for Django</summary>
  
  ## 1. 딕셔너리
  
  - 데이터들을 `대응` 시켜주는 자료형
  - 탐색의 기준인 `키워드` ---- `찾고자 하는 값`을 대응시킴
  - 즉, `key` ---- `value`
  - 🌟 key값은 중복되어서도, 변해서도 안된다!
  - 딕셔너리를 쓰는 경우 : 2 x N 표를 통해 데이터를 표현하고 싶을 때
  
  ## 2. 예외처리
  
  - Python의 오류에는 `파싱에러` 와 `예외`가 있음
  - `파싱에러` : 실행 자체에 영향을 주는 치명적인 오류 == 문법 오류 (예: 오타, 배열 인덱스 오류 등)
  - `예외` : 프로그램 실행 자체를 멈추지는 않음, 실행 중 감지되는 오류 (예: TypeError, NameError, ZeroDivisionError 등)
  - 오류 핸들링(Handling) -> try ••• except ••• finally : 어떤 오류가 발생해도 코드가 실행됨!
  
  🌟 핸들링의 의의 : 프로그램을 `멈춤 없이` 실행시킬 수 있다!
  
  ```python
  try:
   #일단 시도해 볼 것
   #오류가 생길 여지가 있는 코드
  except 발생 오류:
   #발생 오류가 발생했을 경우 실행할 코드
  finally:
   #예외가 발생했든 안 했든
   #최종적으로 무조건 실행할 코드

  try:
     4/0
  except: ZeroDivisionError:
     print("0으로 나눌 수 없습니다.")
  finally:
     print("계산 끝")                # -> 0으로 나눌 수 없습니다. 계산 끝
  ```
  https://docs.python.org/ko/3/tutorial/errors.html
  
  ## 3. 객체와 클래스
  
  - 세상에 있는 모든 것들을 프로그래밍 하고 싶어! -> 세상에 있는 모든 다른 대상(객체)을 관찰
  - 객체를 프로그래밍 할 수 있다면 -> 세상에 있는 다른 객체들도 프로그래밍할 수 있음
  - 이 세상의 모든 객체는 무엇으로 구성되어 있을까? -> `상태`, `동작`
  
  -> 이 세상에 있는 모든 대상들은 `상태`와 `동작`으로 나타낼 수 있다!!
  
  -> **변수**와 **함수**로 표현
  
  ```python
  # 예시
  name = "panda"    # 상태 == 변수
  weight = 120
  age = 20

  def sleepy():     # 동작 == 함수
     if 졸리면:
        잔다

  def hungry();
     if 배고프면:
        먹는다
  ```
  
  ❗️ 세상에 대상들이 한두개가 아님, 상태와 동작을 한 번에 여러개 정의할 수 있어야함 == **객체 지향 프로그래밍**
  - 틀(클래스)를 만들고 달고나(객체) 찍어내기
  ```python
  # 예시 - 판다 세마리를 만들고 싶어
  
  class Panda():
    weight = 120
    age = 20
  
  def sleepy():
    if(졸리면):
      잔다
  def hungry():
    if(배고프면):
      먹는다
  
  panda1 = Panda()
  panda2 = Panda()
  panda3 = Panda()
  ```
  
  ## 4. 모듈, 패키지, 라이브러리
  
  - **모듈** : 가장 작은 단위의 파이썬으로 정의된 파일, `import`를 통해 다른 파일의 모듈을 사용할 수 있음
  - **패키지** : 모듈의 집합, 모듈의 계층 단위
  ```python
  # My Project 폴더에 Data라는 폴더 속에 save.py, get.py, delete.py가 있다면 Data/==패키지
  
  import data.save
  import data.get
  import data.delete
  ```
  - **라이브러리** : 쓸만한 기능들을 미리 모듈/패키지로 만들어 놓은 것, 미리 준비된 모듈 및 패키지
  - Python Standard Library(파이썬 내장함수), Python Package Index(PyPI: 사람들이 만든 라이브러리) 
  - `pip` : Python Package Management System (다운 받은 패키지를 관리하는 툴)
  
  ```python
  $pip install 패키지명         # 패키지 설치
  $pip install 패키지명==1.04   # 특정 버전 지정하여 설치
  $pip search 패키지명          # 패키지 검색
  $pip uninstall 패키지명       # 패키지 제거
  $pip freeze                 # 현재 설치된 패키지와 버전 목록 조회
  ```
</detials>

<details>
  <summary>Web Service, Web Framework</summary>
  - www : World Wide Web, 정보의 그물망 -> url, http, html
  1. URL : 정보 자원이 어디 있는지를 나타내는 표식
  2. HTTP : 정보자원으로 접근하고 통신하게 해 주는 약속, protocol 요청 -> get : "갖다줘" , post = "처리해줘
  3. HTML
  
</details>
