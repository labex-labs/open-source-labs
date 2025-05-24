# 실제로 무언가를 하는 뷰 작성

각 뷰는 두 가지 중 하나를 담당합니다. 요청된 페이지의 콘텐츠를 포함하는 `~django.http.HttpResponse` 객체를 반환하거나 `~django.http.Http404`와 같은 예외를 발생시키는 것입니다. 나머지는 여러분에게 달려 있습니다.

뷰는 데이터베이스에서 레코드를 읽을 수도 있고, 그렇지 않을 수도 있습니다. Django 의 템플릿 시스템과 같은 템플릿 시스템이나 타사 Python 템플릿 시스템을 사용할 수도 있고, 그렇지 않을 수도 있습니다. PDF 파일을 생성하거나, XML 을 출력하거나, 즉석에서 ZIP 파일을 만들 수 있으며, 원하는 Python 라이브러리를 사용하여 원하는 모든 작업을 수행할 수 있습니다.

Django 가 원하는 것은 `~django.http.HttpResponse`입니다. 또는 예외입니다.

편의상 튜토리얼 2 에서 다룬 Django 자체 데이터베이스 API 를 사용해 보겠습니다. 다음은 시스템에서 최신 5 개의 설문 질문을 게시 날짜에 따라 쉼표로 구분하여 표시하는 새로운 `index()` 뷰의 한 가지 시도입니다.

`polls/views.py` 파일을 편집하고 다음과 같이 변경합니다.

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

하지만 여기에는 문제가 있습니다. 페이지의 디자인이 뷰에 하드 코딩되어 있습니다. 페이지의 모양을 변경하려면 이 Python 코드를 편집해야 합니다. 따라서 Django 의 템플릿 시스템을 사용하여 뷰가 사용할 수 있는 템플릿을 만들어 디자인을 Python 과 분리해 보겠습니다.

먼저 `polls` 디렉토리에 `templates`라는 디렉토리를 만듭니다. Django 는 거기에서 템플릿을 찾습니다.

프로젝트의 `TEMPLATES` 설정은 Django 가 템플릿을 로드하고 렌더링하는 방법을 설명합니다. 기본 설정 파일은 `APP_DIRS <TEMPLATES-APP_DIRS>` 옵션이 `True`로 설정된 `DjangoTemplates` 백엔드를 구성합니다. 관례에 따라 `DjangoTemplates`는 각 `INSTALLED_APPS`에서 "templates" 하위 디렉토리를 찾습니다.

방금 만든 `templates` 디렉토리 내에 `polls`라는 다른 디렉토리를 만들고, 그 안에 `index.html`이라는 파일을 만듭니다. 즉, 템플릿은 `polls/templates/polls/index.html`에 있어야 합니다. 위에서 설명한 대로 `app_directories` 템플릿 로더가 작동하는 방식 때문에 Django 내에서 이 템플릿을 `polls/index.html`로 참조할 수 있습니다.

## 템플릿 네임스페이스 (Template namespacing)

이제 템플릿을 `polls/templates`에 직접 넣는 것 (다른 `polls` 하위 디렉토리를 만들지 않고) 으로 해결할 수 있을지도 모르지만, 실제로 좋지 않은 생각입니다. Django 는 이름이 일치하는 첫 번째 템플릿을 선택하며, _다른_ 애플리케이션에 동일한 이름의 템플릿이 있는 경우 Django 는 이를 구별할 수 없습니다.

Django 가 올바른 템플릿을 가리키도록 해야 하며, 이를 보장하는 가장 좋은 방법은 *네임스페이스 (namespacing)*를 사용하는 것입니다. 즉, 해당 템플릿을 애플리케이션 자체의 이름을 딴 _다른_ 디렉토리 안에 넣는 것입니다.

해당 템플릿에 다음 코드를 넣습니다.

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

참고:

튜토리얼을 짧게 만들기 위해 모든 템플릿 예제는 불완전한 HTML 을 사용합니다. 자체 프로젝트에서는 [완전한 HTML 문서](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document)를 사용해야 합니다.

이제 `polls/views.py`의 `index` 뷰를 업데이트하여 템플릿을 사용해 보겠습니다.

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

이 코드는 `polls/index.html`이라는 템플릿을 로드하고 컨텍스트를 전달합니다. 컨텍스트는 템플릿 변수 이름을 Python 객체에 매핑하는 사전입니다.

서버를 다시 실행합니다.

```bash
python manage.py runserver 0.0.0.0:8080
```

브라우저를 "/polls/"로 가리켜 페이지를 로드하면 튜토리얼 2 의 "What's up" 질문이 포함된 글머리 기호 목록이 표시됩니다. 링크는 질문의 상세 페이지를 가리킵니다.

![Django polls index page](../assets/20230908-09-37-26-QMKEbUhb.png)

## 단축키: `~django.shortcuts.render`

템플릿을 로드하고, 컨텍스트를 채우고, 렌더링된 템플릿의 결과로 `~django.http.HttpResponse` 객체를 반환하는 것은 매우 일반적인 관용구입니다. Django 는 단축키를 제공합니다. 다음은 다시 작성된 전체 `index()` 뷰입니다.

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

이러한 모든 뷰에서 이 작업을 수행했으면 더 이상 `~django.template.loader` 및 `~django.http.HttpResponse`를 가져올 필요가 없습니다 (아직 `detail`, `results`, `vote`에 대한 스텁 메서드가 있는 경우 `HttpResponse`를 유지하고 싶을 것입니다).

`~django.shortcuts.render` 함수는 첫 번째 인수로 요청 객체를, 두 번째 인수로 템플릿 이름을, 세 번째 인수로 선택적 사전을 사용합니다. 주어진 컨텍스트로 렌더링된 주어진 템플릿의 `~django.http.HttpResponse` 객체를 반환합니다.
