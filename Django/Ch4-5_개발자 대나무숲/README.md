## CRUD

- `Create` : 생성
- `Read` : 읽기
- `Update` : 갱신
- `Delete` : 삭제

## Database

- 웹프레임워크랑 데이터베이스는 서로 관련이 X
- 장고에서 db 활용하려면 장고랑 연결, 상호작용 해야한다
- `DBMS` : 데이터베이스 관리시스템을 
- MySQL, ORACLE, SQL Server, SQLite
- `RDBMS` : 데이터베이스 안의 데이터들을 표처럼 활용
- `SQL` : 데이터베이스에 접근하고 조작하는 언어 
- `Primary Key` : 반드시 존재 (Null값 X), 다른 값과 중복X
- `Foreign Key`(외래키) : 다른 테이블의 특정 컬럼, 혹은 다른 테이블을 참조할 수 있는 키 

<br>

## Models


- `ORM` (Object Relational Mapping ): 장고가 객체로써(파이썬의 객체로써) DB테이블과 상호작용하여 표현 가능
- 객체를 이용해서 데이터베이스를 조작

- `[models.py](http://models.py)` 안에 `class` 로 `table` 표현 → class table을 만들 수 있음

```python
from django.db import models

class Student(models.Model):
  studentNumber = models.IntegerField()
  name = models.CharField()
  picture = models.ImageField()
  classes = models.TextField()
```

- `migration` 을 사용해야 class가 table로 변함
(`database migration`)
- 데이터베이스 마이그레이션을 위해 사용하는 명령어

> `$ python manage.py migrate`  : 데이터 초기화, 변경사항 반영

<br>

## HTML, Django Form

```
1. HTML Form 이용하기
2. Django Form 이용하기
3. Django modelForm 이용하기
```

- 장고의 GET요청 & POST요청

> 입력값을 받을 수 있는 HTML을 줘야 함 

> 입력한 내용을 데이터베이스에 저장 

> FORM에서 입력한 내용을 처리

<br>

## QuerySet

- 데이터베이스로부터 전달받은 객체 목록

```html
{% for post in posts %}
    <h3> 제목: {{ post.title }}</h3>
    <h4> 작성날짜 : {{ post.date }}</h4>

    {{ post.body }}

{% endfor %}
```
<br>

## Detail page 구현하기

detail이라는 url로 이동하기 : `<a href="{% url 'detail' [post.id](http://post.id/) %}"><h3> 제목: {{ post.title }}</h3></a>`

int형 blog_id 인자로 넘겨주기 : `path('detail/int:blog_id', views.detail, name='detail'),`

pk값을 이용해 특정 모델 객체 하나만 갖고오기 : `get_object_or_404()`

<br>

## 파일 업로드

```html
<h1>제목</h1>
{{blog_detail.title}}

<h2>날짜</h2>
{{blog_detail.date}}

<h3>본문</h3>
{{blog_detail.body}}

<h3>본문</h3>
{% if blog_detail.photo %}
    <!--사진 찍어주기-->
    {{blog_detail.photo.url}}
    <img src="{{blog_detail.photo.url}}" alt="" height="600">

{% endif %}
```
<br>

## 로그인/로그아웃

`$ python manage.py startapp accounts` : 앱 만들기
`from django.contrib import auth` : 내장 기능 가져오기
`python manage.py createsuperuser` : 관리자 계정 만들기

```python
def edit(request, blog_id):
    post = Blog.objects.get(id=blog_id)    # 수정하고자 하는 객체 갖고오기
    if request.method == "POST":            # 만일 request method가 POST라면
        form = BlogForm(request.POST, request.FILES)    # 입력 내용을 갖고와서
        if form.is_valid():                             # 입력 내용 검수하고
            post.title = form.cleaned_data['title']     # 입력 내용 중 title을 수정하고자 하는 객체의 title에 저장!
            post.body = form.cleaned_data['body']       # 입력 내용 중 body를 수정하고자 하는 객체의 body에 저장!
            post.save()                                 # 그리고 수정된 값을 저장한 객체는 저장
            return redirect('/detail/'+str(post.pk))      # 수정이 되었으면 detail 페이지(해당 그 게시물 페이지)로 이동
    else:                                        # 만일 request method가 GET이면
        form = BlogForm()                  
        return render(request, 'form_edit.html',{'form':form})  # 입력 공간 갖다주기
```
