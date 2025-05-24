# 템플릿 시스템 사용하기

설문 애플리케이션의 `detail()` 뷰로 돌아가 보겠습니다. 컨텍스트 변수 `question`이 주어지면, `polls/detail.html` 템플릿은 다음과 같을 수 있습니다.

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

템플릿 시스템은 변수 속성에 접근하기 위해 점 조회 구문을 사용합니다. `{{ question.question_text }}`의 예에서, Django 는 먼저 객체 `question`에 대한 딕셔너리 조회를 수행합니다. 실패하면, 속성 조회를 시도합니다. 이 경우 작동합니다. 속성 조회가 실패하면, 목록 인덱스 조회를 시도했을 것입니다.

메서드 호출은 `{% for %}<for>` 루프에서 발생합니다. `question.choice_set.all`은 Python 코드 `question.choice_set.all()`로 해석되어 `Choice` 객체의 반복 가능한 객체를 반환하며, `{% for %}<for>` 태그에서 사용하기에 적합합니다.
