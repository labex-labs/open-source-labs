# 404 오류 발생시키기

이제 주어진 설문에 대한 질문 텍스트를 표시하는 페이지인 질문 상세 뷰를 살펴보겠습니다. 다음은 뷰입니다.

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question


# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

여기서 새로운 개념은 다음과 같습니다. 요청된 ID 의 질문이 존재하지 않으면 뷰가 `~django.http.Http404` 예외를 발생시킵니다.

`polls/detail.html` 템플릿에 넣을 수 있는 내용에 대해서는 잠시 후에 논의하겠지만, 위의 예제를 빠르게 작동시키려면 다음 내용만 포함하는 파일이 있으면 됩니다.

```html+django
{{ question }}
```

지금은 이것으로 시작할 수 있습니다.

## 단축키: `~django.shortcuts.get_object_or_404`

`~django.db.models.query.QuerySet.get`을 사용하고 객체가 존재하지 않으면 `~django.http.Http404`를 발생시키는 것은 매우 일반적인 관용구입니다. Django 는 단축키를 제공합니다. 다음은 다시 작성된 `detail()` 뷰입니다.

```python
from django.shortcuts import get_object_or_404, render

from .models import Question


# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

`~django.shortcuts.get_object_or_404` 함수는 Django 모델을 첫 번째 인수로, 임의의 수의 키워드 인수를 두 번째 인수로 사용하며, 이를 모델의 매니저의 `~django.db.models.query.QuerySet.get` 함수에 전달합니다. 객체가 존재하지 않으면 `~django.http.Http404`를 발생시킵니다.

왜 `~django.shortcuts.get_object_or_404` 도우미 함수를 사용하여 상위 수준에서 `~django.core.exceptions.ObjectDoesNotExist` 예외를 자동으로 포착하거나 모델 API 가 `~django.core.exceptions.ObjectDoesNotExist` 대신 `~django.http.Http404`를 발생시키지 않습니까?

그렇게 하면 모델 계층이 뷰 계층에 결합되기 때문입니다. Django 의 주요 설계 목표 중 하나는 느슨한 결합을 유지하는 것입니다. 일부 제어된 결합은 `django.shortcuts` 모듈에 도입됩니다.

`~django.shortcuts.get_list_or_404` 함수도 있으며, `~django.shortcuts.get_object_or_404`와 동일하게 작동합니다. 단, `~django.db.models.query.QuerySet.get` 대신 `~django.db.models.query.QuerySet.filter`를 사용합니다. 목록이 비어 있으면 `~django.http.Http404`를 발생시킵니다.
