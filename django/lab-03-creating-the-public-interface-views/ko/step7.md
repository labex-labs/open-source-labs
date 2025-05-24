# URL 이름 네임스페이스 지정하기

튜토리얼 프로젝트에는 `polls`라는 하나의 앱만 있습니다. 실제 Django 프로젝트에서는 5 개, 10 개, 20 개 이상의 앱이 있을 수 있습니다. Django 는 어떻게 그들 사이에서 URL 이름을 구별할까요? 예를 들어, `polls` 앱에는 `detail` 뷰가 있고, 블로그용으로 동일한 프로젝트의 앱에도 있을 수 있습니다. `{% url %}` 템플릿 태그를 사용할 때 Django 가 어떤 앱 뷰를 URL 에 대해 생성해야 하는지 알 수 있도록 하려면 어떻게 해야 할까요?

해답은 URLconf 에 네임스페이스를 추가하는 것입니다. `polls/urls.py` 파일에서 `app_name`을 추가하여 애플리케이션 네임스페이스를 설정합니다.

```python
from django.urls import path

from . import views

app_name = "polls"
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

이제 `polls/index.html` 템플릿을 다음에서 변경합니다.

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

네임스페이스가 지정된 상세 뷰를 가리키도록 변경합니다.

```html+django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

![URL 네임스페이스 지정 예시](../assets/20230908-09-58-22-qkl9l0DT.png)

뷰 작성이 익숙해지면, **Form Processing and Cutting Down Our Code**를 읽고 폼 처리 및 제네릭 뷰에 대한 기본 사항을 알아보세요.
