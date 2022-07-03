## url mapping

```python
# views.py
from django.shortcuts import render

# Create your views here.
def board(request):
    return render(request, 'board.html')

def boardfirst(request):
    return render(request, 'boardfirst.html')
```

```python
# urls.py
from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist), #http://127.0.0.1:8000/products/
    path('first/', views.productfirst), #http://127.0.0.1:8000/products/first/
]


#127.0.0.1:8000/products/first에 대해서 productfirst함수가 실행된다.
```
<br>

## static

- 웹 서비스 내부 데이터는 Static과 Media 두 가지
- Static : 웹 서비스 내부에서 사용자를 위해서 미리 준비한 데이터
- Media : 사용자가 업로드한 사용자에 의한 데이터
- `STATICFILES_DIRS`: static 파일들의 경로 작성
- `STATIC_ROOT`: static 파일들을 복사하여 모아 놓을 경로를 설정
- 배포시 `python manage.py collectstatic` 명령어 활용해서 static 파일들을 모두 모을 수 있음
- `STATIC_URL`: static 파일을 제공할 url

<br>

## bootstrap

- bootstrap : 이미 만들어놓은 웹사이트의 꾸밈 요소

> 1. Bootstrap 관련 코드를 직접 다운 받아 설치
> 2. CDN 이용 (url 코드를 복사해오는 것)

#### 장고에서 bootstrap 가져오기
- settings.py에 static경로 지정해주기

- html파일에 bootstrap link 걸어주기 
- href 속성 작성할 때 템플릿 언어로 작성

`<link rel = "stylesheet" type="text/css" href="{% static ‘scc/bootstrap.min.css’ %}">`

`<script src="{% static 'js/bootstrap.min.js' %}"></script>`

<br>

## template

- `{% url 'url name' %}` : 장고가 관리해주는 url name
- `{% block content %}`
- `{% endblock %}`
