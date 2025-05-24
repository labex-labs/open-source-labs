# 뷰 추가 작성

이제 `polls/views.py`에 몇 개의 뷰를 더 추가해 보겠습니다. 이 뷰들은 인수를 받기 때문에 약간 다릅니다.

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

다음 `~django.urls.path` 호출을 추가하여 이러한 새로운 뷰를 `polls.urls` 모듈에 연결합니다.

`polls/urls.py` 파일을 편집하고 다음 줄을 추가합니다.

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

이제 서버를 다시 실행합니다.

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

**Web 8080** 탭으로 전환하여 `/polls/34/`를 입력합니다. `detail()` 메서드를 실행하고 URL 에 제공한 ID 를 표시합니다. `/polls/34/results/` 및 `/polls/34/vote/`도 시도해 보세요. 이러한 URL 은 자리 표시자 결과 및 투표 페이지를 표시합니다.

![Django URL routing diagram](../assets/20230908-09-30-06-2n54ROPe.png)

어떤 사람이 웹사이트에서 페이지를 요청하면 (예: `/polls/34/`), Django 는 `ROOT_URLCONF` 설정에 의해 지정되어 있기 때문에 `mysite.urls` Python 모듈을 로드합니다. `urlpatterns`라는 변수를 찾고 패턴을 순서대로 탐색합니다. `'polls/'`에서 일치하는 항목을 찾은 후 일치하는 텍스트 (`"polls/"`) 를 제거하고 나머지 텍스트 (`"34/"`) 를 추가 처리를 위해 'polls.urls' URLconf 로 보냅니다. 거기에서 `'<int:question_id>/'`와 일치하여 다음과 같이 `detail()` 뷰를 호출합니다.

```python
detail(request=<HttpRequest object>, question_id=34)
```

`question_id=34` 부분은 `<int:question_id>`에서 가져옵니다. 꺾쇠 괄호 ("<>") 를 사용하면 URL 의 일부를 "캡처"하여 뷰 함수에 키워드 인수로 보냅니다. 문자열의 `question_id` 부분은 일치하는 패턴을 식별하는 데 사용될 이름을 정의하고, `int` 부분은 이 URL 경로의 일부와 일치해야 하는 패턴을 결정하는 변환기 (converter) 입니다. 콜론 (":") 은 변환기와 패턴 이름을 구분합니다.
