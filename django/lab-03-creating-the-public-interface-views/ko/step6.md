# 템플릿에서 하드코딩된 URL 제거하기

`polls/index.html` 템플릿에서 질문에 대한 링크를 작성했을 때, 링크가 다음과 같이 부분적으로 하드코딩되었던 것을 기억하실 겁니다.

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

이 하드코딩된, 긴밀하게 결합된 접근 방식의 문제는 템플릿이 많은 프로젝트에서 URL 을 변경하는 것이 어려워진다는 것입니다. 하지만, `polls.urls` 모듈의 `~django.urls.path` 함수에서 name 인수를 정의했으므로, `{% url %}` 템플릿 태그를 사용하여 URL 구성에 정의된 특정 URL 경로에 대한 의존성을 제거할 수 있습니다.

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

이것이 작동하는 방식은 `polls.urls` 모듈에 지정된 대로 URL 정의를 찾는 것입니다. 'detail'의 URL 이름이 아래에서 정확히 어디에 정의되어 있는지 확인할 수 있습니다.

```python
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
```

설문 상세 뷰의 URL 을 다른 것으로 변경하고 싶다면, 예를 들어 `polls/specifics/12/`와 같이 변경하고 싶다면, 템플릿 (또는 템플릿들) 에서 변경하는 대신 `polls/urls.py`에서 변경합니다.

> 템플릿을 전혀 변경할 필요가 없습니다.

```python
# added the word 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
