# 관련 객체 추가

자, `Question` 관리자 페이지가 있지만, `Question`에는 여러 개의 `Choice`가 있으며, 관리자 페이지는 선택 사항을 표시하지 않습니다.

아직은요.

이 문제를 해결하는 두 가지 방법이 있습니다. 첫 번째는 `Question`과 마찬가지로 `Choice`를 관리자에 등록하는 것입니다.

```python
from django.contrib import admin

from .models import Choice, Question

# ...
admin.site.register(Choice)
```

이제 "Choices"는 Django 관리자에서 사용 가능한 옵션입니다. "Add choice" 폼은 다음과 같습니다.

![Add Choice form interface](../assets/20230908-16-09-57-eCXIdjZu.png)

해당 폼에서 "Question" 필드는 데이터베이스의 모든 질문을 포함하는 선택 상자입니다. Django 는 `~django.db.models.ForeignKey`가 관리자에서 `<select>` 상자로 표시되어야 함을 알고 있습니다. 이 경우, 현재 시점에는 질문이 하나만 존재합니다.

또한 "Question" 옆에 있는 "Add another question" 링크에 유의하십시오. 다른 객체와의 `ForeignKey` 관계가 있는 모든 객체는 이를 무료로 얻습니다. "Add another question"을 클릭하면 "Add question" 폼이 있는 팝업 창이 나타납니다. 해당 창에서 질문을 추가하고 "Save"를 클릭하면 Django 는 질문을 데이터베이스에 저장하고 보고 있는 "Add choice" 폼에서 선택된 선택 사항으로 동적으로 추가합니다.

하지만, 실제로 이것은 `Choice` 객체를 시스템에 추가하는 비효율적인 방법입니다. `Question` 객체를 생성할 때 직접적으로 여러 개의 Choices 를 추가할 수 있다면 더 좋을 것입니다. 그렇게 해 봅시다.

`Choice` 모델에 대한 `register()` 호출을 제거합니다. 그런 다음 `Question` 등록 코드를 다음과 같이 편집합니다.

```python
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

이것은 Django 에게 다음과 같이 알려줍니다. "`Choice` 객체는 `Question` 관리자 페이지에서 편집됩니다. 기본적으로 3 개의 선택 사항에 대한 충분한 필드를 제공합니다."

"Add question" 페이지를 로드하여 모양을 확인합니다.

![Question admin with choices](../assets/20230908-16-11-09-tVqaXrGB.png)

다음과 같이 작동합니다. `extra`로 지정된 대로 관련 Choices 에 대한 세 개의 슬롯이 있으며, 이미 생성된 객체의 "Change" 페이지로 돌아올 때마다 세 개의 추가 슬롯이 더 제공됩니다.

현재 세 개의 슬롯 끝에서 "Add another Choice" 링크를 찾을 수 있습니다. 이를 클릭하면 새 슬롯이 추가됩니다. 추가된 슬롯을 제거하려면 추가된 슬롯의 오른쪽 상단에 있는 X 를 클릭하면 됩니다. 이 이미지는 추가된 슬롯을 보여줍니다.

![Additional slot added dynamically](../assets/admin14t.png)

하지만 한 가지 작은 문제가 있습니다. 관련 `Choice` 객체를 입력하기 위한 모든 필드를 표시하는 데 많은 화면 공간이 필요합니다. 이러한 이유로 Django 는 인라인 관련 객체를 표시하는 표 형식의 방법을 제공합니다. 이를 사용하려면 `ChoiceInline` 선언을 다음과 같이 변경합니다.

```python
class ChoiceInline(admin.TabularInline):
    ...
```

`TabularInline` ( `StackedInline` 대신) 을 사용하면 관련 객체가 더 간결한 테이블 기반 형식으로 표시됩니다.

![Tabular inline choices display](../assets/20230908-16-12-24-1nqRkbAI.png)

"Add another Choice" 버튼을 사용하여 추가된 행과 이미 저장된 행을 제거할 수 있는 추가 "Delete?" 열이 있음에 유의하십시오.
