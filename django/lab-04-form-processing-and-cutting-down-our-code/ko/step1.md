# 최소한의 폼 작성하기

마지막 튜토리얼에서 다룬 설문 상세 템플릿 (`polls/detail.html`) 을 업데이트하여 템플릿에 HTML `<form>` 요소를 포함하도록 하겠습니다.

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

간단한 설명:

- 위의 템플릿은 각 질문 선택 항목에 대한 라디오 버튼을 표시합니다. 각 라디오 버튼의 `value`는 관련 질문 선택 항목의 ID 입니다. 각 라디오 버튼의 `name`은 `"choice"`입니다. 즉, 누군가 라디오 버튼 중 하나를 선택하고 폼을 제출하면 `choice=#` 형식의 POST 데이터를 전송합니다. 여기서 #은 선택한 선택 항목의 ID 입니다. 이것이 HTML 폼의 기본 개념입니다.
- 폼의 `action`을 `{% url 'polls:vote' question.id %}`로 설정하고 `method="post"`를 설정했습니다. `method="post"`를 사용하는 것 ( `method="get"`와 반대로) 은 매우 중요합니다. 이 폼을 제출하는 행위가 서버 측 데이터를 변경하기 때문입니다. 서버 측 데이터를 변경하는 폼을 만들 때는 항상 `method="post"`를 사용하십시오. 이 팁은 Django 에만 국한된 것이 아니라 일반적인 웹 개발 관행입니다.
- `forloop.counter`는 `for` 태그가 루프를 몇 번 반복했는지 나타냅니다.
- POST 폼을 만들고 있으므로 (데이터를 수정하는 효과가 있을 수 있음) Cross Site Request Forgeries (CSRF, 교차 사이트 요청 위조) 에 대해 걱정해야 합니다. 다행히 Django 는 이를 방지하는 데 도움이 되는 시스템을 제공하므로 너무 걱정할 필요는 없습니다. 간단히 말해서, 내부 URL 을 대상으로 하는 모든 POST 폼은 `{% csrf_token %}` 템플릿 태그를 사용해야 합니다.

이제 제출된 데이터를 처리하고 이를 사용하여 무언가를 수행하는 Django 뷰를 만들어 보겠습니다. 기억하세요, `**Creating the Public Interface Views**`에서 다음 줄을 포함하는 설문 애플리케이션에 대한 URLconf 를 만들었습니다.

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

또한 `vote()` 함수의 더미 구현을 만들었습니다. 실제 버전을 만들어 보겠습니다. 다음을 `polls/views.py`에 추가합니다.

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

이 코드는 이 튜토리얼에서 아직 다루지 않은 몇 가지 사항을 포함합니다.

- `request.POST <django.http.HttpRequest.POST>`는 키 이름으로 제출된 데이터에 액세스할 수 있는 딕셔너리 유사 객체입니다. 이 경우 `request.POST['choice']`는 선택한 선택 항목의 ID 를 문자열로 반환합니다. `request.POST <django.http.HttpRequest.POST>` 값은 항상 문자열입니다.

  Django 는 `request.GET <django.http.HttpRequest.GET>`도 제공하여 GET 데이터에 동일한 방식으로 액세스할 수 있습니다. 하지만 데이터가 POST 호출을 통해서만 변경되도록 하기 위해 코드에서 명시적으로 `request.POST <django.http.HttpRequest.POST>`를 사용하고 있습니다.

- `request.POST['choice']`는 POST 데이터에 `choice`가 제공되지 않은 경우 `KeyError`를 발생시킵니다. 위의 코드는 `KeyError`를 확인하고 `choice`가 제공되지 않은 경우 오류 메시지와 함께 질문 폼을 다시 표시합니다.

- 선택 항목 수를 증가시킨 후 코드는 일반 `~django.http.HttpResponse` 대신 `~django.http.HttpResponseRedirect`를 반환합니다. `~django.http.HttpResponseRedirect`는 단일 인수를 사용합니다. 즉, 사용자가 리디렉션될 URL 입니다 (이 경우 URL 을 구성하는 방법은 다음 사항을 참조하십시오).

  위의 Python 주석에서 언급했듯이 POST 데이터를 성공적으로 처리한 후에는 항상 `~django.http.HttpResponseRedirect`를 반환해야 합니다. 이 팁은 Django 에만 국한된 것이 아니라 일반적인 웹 개발 관행입니다.

- 이 예제에서는 `~django.http.HttpResponseRedirect` 생성자에서 `~django.urls.reverse` 함수를 사용하고 있습니다. 이 함수는 뷰 함수에서 URL 을 하드코딩하는 것을 피하는 데 도움이 됩니다. 제어 권한을 넘겨주고 싶은 뷰의 이름과 해당 뷰를 가리키는 URL 패턴의 변수 부분을 제공합니다. 이 경우, `**Creating the Public Interface Views**`에서 설정한 URLconf 를 사용하면 이 `~django.urls.reverse` 호출은 다음과 같은 문자열을 반환합니다.

      "/polls/3/results/"

  여기서 `3`은 `question.id`의 값입니다. 이 리디렉션된 URL 은 `results` 뷰를 호출하여 최종 페이지를 표시합니다.

`**Creating the Public Interface Views**`에서 언급했듯이 `request`는 `~django.http.HttpRequest` 객체입니다. `~django.http.HttpRequest` 객체에 대한 자세한 내용은 `request and response documentation </ref/request-response>`를 참조하십시오.

누군가 질문에 투표한 후 `vote()` 뷰는 질문에 대한 결과 페이지로 리디렉션됩니다. 해당 뷰를 작성해 보겠습니다.

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

이것은 `**Creating the Public Interface Views**`의 `detail()` 뷰와 거의 동일합니다. 유일한 차이점은 템플릿 이름입니다. 이 중복은 나중에 수정하겠습니다.

이제 `polls/results.html` 템플릿을 만듭니다.

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

이제 브라우저에서 `/polls/1/`로 이동하여 질문에 투표하십시오. 투표할 때마다 업데이트되는 결과 페이지가 표시됩니다. 선택 항목을 선택하지 않고 폼을 제출하면 오류 메시지가 표시됩니다.

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![Poll voting form interface](../assets/20230908-10-37-07-p9ewKbe6.png)

**참고:**

`vote()` 뷰에 대한 코드에는 작은 문제가 있습니다. 먼저 데이터베이스에서 `selected_choice` 객체를 가져온 다음 `votes`의 새 값을 계산한 다음 다시 데이터베이스에 저장합니다. 웹사이트의 두 사용자가 _정확히 동시에_ 투표하려고 하면 문제가 발생할 수 있습니다. 동일한 값 (예: 42) 이 `votes`에 대해 검색됩니다. 그런 다음 두 사용자 모두에 대해 새 값 43 이 계산되어 저장되지만 예상 값은 44 입니다.

이것을 *경쟁 조건 (race condition)*이라고 합니다. 관심이 있다면 `avoiding-race-conditions-using-f`를 읽고 이 문제를 해결하는 방법을 배울 수 있습니다.
