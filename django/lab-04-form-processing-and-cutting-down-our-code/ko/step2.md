# 제네릭 뷰 사용: 코드가 적을수록 좋습니다

`detail()` ( `**Creating the Public Interface Views**`에서) 및 `results()` 뷰는 매우 짧으며 위에서 언급했듯이 중복됩니다. 설문 목록을 표시하는 `index()` 뷰도 유사합니다.

이러한 뷰는 기본 웹 개발의 일반적인 경우를 나타냅니다. URL 에서 전달된 매개변수에 따라 데이터베이스에서 데이터를 가져오고, 템플릿을 로드하고, 렌더링된 템플릿을 반환합니다. 이것이 매우 일반적이기 때문에 Django 는 "제네릭 뷰" 시스템이라는 바로 가기를 제공합니다.

제네릭 뷰는 일반적인 패턴을 추상화하여 앱을 작성하기 위해 Python 코드를 작성할 필요조차 없게 만듭니다.

설문 앱을 제네릭 뷰 시스템을 사용하도록 변환하여 자체 코드를 많이 삭제할 수 있습니다. 변환을 위해 몇 가지 단계를 거쳐야 합니다. 다음을 수행합니다.

1. URLconf 를 변환합니다.
2. 오래되고 필요 없는 일부 뷰를 삭제합니다.
3. Django 의 제네릭 뷰를 기반으로 하는 새 뷰를 소개합니다.

자세한 내용은 계속 읽어보세요.

> 왜 코드 셔플인가요?

일반적으로 Django 앱을 작성할 때 제네릭 뷰가 문제에 적합한지 평가하고 처음부터 사용하며 중간에 코드를 리팩터링하는 대신 사용합니다. 그러나 이 튜토리얼은 핵심 개념에 집중하기 위해 지금까지 의도적으로 "어려운 방법"으로 뷰를 작성하는 데 중점을 두었습니다.

계산기를 사용하기 전에 기본적인 수학을 알아야 합니다.

## URLconf 수정

먼저 `polls/urls.py` URLconf 를 열고 다음과 같이 변경합니다.

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

두 번째 및 세 번째 패턴의 경로 문자열에서 일치하는 패턴의 이름이 `<question_id>`에서 `<pk>`로 변경되었음에 유의하십시오.

## 뷰 수정

다음으로, 이전 `index`, `detail` 및 `results` 뷰를 제거하고 대신 Django 의 제네릭 뷰를 사용합니다. 이렇게 하려면 `polls/views.py` 파일을 열고 다음과 같이 변경합니다.

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    ...  # same as above, no changes needed.
```

여기서는 두 개의 제네릭 뷰를 사용하고 있습니다: `~django.views.generic.list.ListView` 및 `~django.views.generic.detail.DetailView`. 각각, 이 두 뷰는 "객체 목록 표시" 및 "특정 유형의 객체에 대한 상세 페이지 표시"의 개념을 추상화합니다.

- 각 제네릭 뷰는 어떤 모델을 사용할지 알아야 합니다. 이는 `model` 속성을 사용하여 제공됩니다.
- `~django.views.generic.detail.DetailView` 제네릭 뷰는 URL 에서 캡처된 기본 키 값을 `"pk"`로 호출할 것으로 예상하므로 제네릭 뷰에 대해 `question_id`를 `pk`로 변경했습니다.

기본적으로 `~django.views.generic.detail.DetailView` 제네릭 뷰는 `<app name>/<model name>_detail.html`이라는 템플릿을 사용합니다. 이 경우 `"polls/question_detail.html"` 템플릿을 사용합니다. `template_name` 속성은 Django 에 자동 생성된 기본 템플릿 이름 대신 특정 템플릿 이름을 사용하도록 지시하는 데 사용됩니다. 또한 `results` 목록 뷰에 대해 `template_name`을 지정합니다. 이렇게 하면 결과 뷰와 상세 뷰가 렌더링될 때 서로 다른 모양을 갖도록 보장합니다. 이는 둘 다 백그라운드에서 `~django.views.generic.detail.DetailView`이기 때문입니다.

마찬가지로, `~django.views.generic.list.ListView` 제네릭 뷰는 `<app name>/<model name>_list.html`이라는 기본 템플릿을 사용합니다. `template_name`을 사용하여 `~django.views.generic.list.ListView`에 기존의 `"polls/index.html"` 템플릿을 사용하도록 지시합니다.

튜토리얼의 이전 부분에서 템플릿은 `question` 및 `latest_question_list` 컨텍스트 변수를 포함하는 컨텍스트와 함께 제공되었습니다. `DetailView`의 경우 `question` 변수가 자동으로 제공됩니다. Django 모델 (`Question`) 을 사용하고 있으므로 Django 는 컨텍스트 변수에 적절한 이름을 결정할 수 있습니다. 그러나 ListView 의 경우 자동 생성된 컨텍스트 변수는 `question_list`입니다. 이를 재정의하기 위해 `context_object_name` 속성을 제공하여 `latest_question_list`를 사용하도록 지정합니다. 다른 접근 방식으로, 새 기본 컨텍스트 변수에 맞게 템플릿을 변경할 수 있습니다. 하지만 원하는 변수를 사용하도록 Django 에 지시하는 것이 훨씬 쉽습니다.

서버를 실행하고 제네릭 뷰를 기반으로 하는 새 설문 앱을 사용하십시오.
