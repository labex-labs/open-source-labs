# 관리자 폼 커스터마이징

`Question` 모델을 `admin.site.register(Question)`으로 등록함으로써 Django 는 기본 폼 표현을 구성할 수 있었습니다. 종종 관리자 폼의 모양과 작동 방식을 커스터마이징하고 싶을 것입니다. 객체를 등록할 때 원하는 옵션을 Django 에 알려줌으로써 이를 수행합니다.

편집 폼에서 필드의 순서를 변경하여 이 작업이 어떻게 작동하는지 살펴보겠습니다. `admin.site.register(Question)` 라인을 다음으로 바꿉니다.

`~/project/mysite/polls/admin.py` 파일을 다음과 같이 편집합니다.

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

모델에 대한 관리자 옵션을 변경해야 할 때마다 이 패턴을 따릅니다. 즉, 모델 관리자 클래스를 생성한 다음 `admin.site.register()`에 두 번째 인수로 전달합니다.

Django 개발 서버를 실행합니다.

```bash
cd ~/project/mysite
python manage.py runserver
```

Firefox 또는 데스크톱 환경에서 `http://127.0.0.1:8000/admin/`을 열고 "Questions" 링크를 클릭합니다. 다음과 같은 폼이 표시됩니다.

위의 특정 변경 사항은 "게시 날짜"가 "질문" 필드 앞에 오도록 합니다.

![Admin form field reorder](../assets/20230908-16-06-41-wiBfnHS8.png)

필드가 두 개뿐이므로 인상적이지 않지만, 수십 개의 필드가 있는 관리자 폼의 경우 직관적인 순서를 선택하는 것이 중요한 사용성 세부 사항입니다.

그리고 수십 개의 필드가 있는 폼에 대해 말하자면, 폼을 필드셋으로 분할하고 싶을 수 있습니다.

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

`~django.contrib.admin.ModelAdmin.fieldsets`의 각 튜플의 첫 번째 요소는 필드셋의 제목입니다. 이제 폼은 다음과 같습니다.

![Admin form with fieldsets](../assets/20230908-16-08-19-HOzMJWFG.png)
