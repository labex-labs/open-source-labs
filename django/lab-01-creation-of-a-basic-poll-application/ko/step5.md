# 첫 번째 뷰 작성

첫 번째 뷰를 작성해 보겠습니다. `polls/views.py` 파일을 열고 다음 Python 코드를 입력합니다.

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

이것은 Django 에서 가능한 가장 간단한 뷰입니다. 뷰를 호출하려면 URL 에 매핑해야 하며, 이를 위해 URLconf 가 필요합니다.

polls 디렉토리에 URLconf 를 생성하려면 `urls.py`라는 파일을 만듭니다. 이제 앱 디렉토리는 다음과 같이 표시됩니다.

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

`polls/urls.py` 파일에 다음 코드를 포함합니다.

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

다음 단계는 루트 URLconf 가 `polls.urls` 모듈을 가리키도록 하는 것입니다. `mysite/urls.py`에서 `django.urls.include`에 대한 import 를 추가하고 `urlpatterns` 목록에 `~django.urls.include`를 삽입하여 다음과 같이 만듭니다.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

`~django.urls.include` 함수는 다른 URLconf 를 참조할 수 있도록 합니다. Django 가 `~django.urls.include`를 발견할 때마다 해당 지점까지 일치하는 URL 의 모든 부분을 잘라내고 나머지 문자열을 포함된 URLconf 로 보내 추가 처리를 수행합니다.

`~django.urls.include`의 아이디어는 URL 을 쉽게 플러그 앤 플레이할 수 있도록 하는 것입니다. 설문 조사가 자체 URLconf (`polls/urls.py`) 에 있으므로 "/polls/" 또는 "/fun_polls/" 또는 "/content/polls/" 또는 다른 경로 루트 아래에 배치할 수 있으며 앱은 계속 작동합니다.

> `~django.urls.include()`를 언제 사용해야 할까요?
> 다른 URL 패턴을 포함할 때는 항상 `include()`를 사용해야 합니다. `admin.site.urls`는 이에 대한 유일한 예외입니다.

이제 `index` 뷰를 URLconf 에 연결했습니다. 다음 명령으로 작동하는지 확인합니다.

```bash
python manage.py runserver 0.0.0.0:8080
```

브라우저에서 <http://<url>/polls/>로 이동하면 `index` 뷰에서 정의한 텍스트 "_Hello, world. You're at the polls index._"가 표시됩니다.

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

`~django.urls.path` 함수는 route, view, kwargs, name 의 네 가지 인수를 전달받습니다. 이 시점에서 이러한 인수가 무엇을 위한 것인지 검토할 가치가 있습니다.

## `~django.urls.path` 인수: `route`

`route`는 URL 패턴을 포함하는 문자열입니다. 요청을 처리할 때 Django 는 `urlpatterns`의 첫 번째 패턴에서 시작하여 목록을 내려가면서 요청된 URL 을 각 패턴과 비교하여 일치하는 항목을 찾을 때까지 비교합니다.

패턴은 GET 및 POST 매개변수 또는 도메인 이름을 검색하지 않습니다. 예를 들어 `https://www.example.com/myapp/`에 대한 요청에서 URLconf 는 `myapp/`을 찾습니다. `https://www.example.com/myapp/?page=3`에 대한 요청에서 URLconf 는 `myapp/`도 찾습니다.

## `~django.urls.path` 인수: `view`

Django 가 일치하는 패턴을 찾으면 첫 번째 인수로 `~django.http.HttpRequest` 객체를, route 에서 "캡처된" 값을 키워드 인수로 사용하여 지정된 뷰 함수를 호출합니다. 잠시 후에 이에 대한 예를 제공하겠습니다.

## `~django.urls.path` 인수: `kwargs`

임의의 키워드 인수는 대상 뷰에 딕셔너리로 전달할 수 있습니다. 이 튜토리얼에서는 Django 의 이 기능을 사용하지 않겠습니다.

## `~django.urls.path` 인수: `name`

URL 의 이름을 지정하면 Django 의 다른 곳, 특히 템플릿 내에서 모호하지 않게 참조할 수 있습니다. 이 강력한 기능을 사용하면 단일 파일만 수정하면서 프로젝트의 URL 패턴을 전역적으로 변경할 수 있습니다.
