# 관리자 변경 목록 커스터마이징

이제 Question 관리자 페이지가 보기 좋게 되었으니, 시스템의 모든 질문을 표시하는 "변경 목록" 페이지를 약간 수정해 보겠습니다.

현재 모습은 다음과 같습니다.

![Polls change list page](../assets/admin04t.png)

기본적으로 Django 는 각 객체의 `str()`을 표시합니다. 하지만 개별 필드를 표시할 수 있다면 더 유용할 때가 있습니다. 이를 위해 `~django.contrib.admin.ModelAdmin.list_display` 관리자 옵션을 사용합니다. 이 옵션은 객체의 변경 목록 페이지에 열로 표시할 필드 이름의 튜플입니다.

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date"]
```

확실하게 하기 위해 `**Set Up the Database**`에서 `was_published_recently()` 메서드도 포함해 보겠습니다.

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

이제 질문 변경 목록 페이지는 다음과 같습니다.

![Question change list view](../assets/20230908-16-14-08-GNY2lggF.png)

해당 값으로 정렬하려면 열 머리글을 클릭할 수 있습니다. 단, 임의의 메서드의 출력으로 정렬하는 것은 지원되지 않으므로 `was_published_recently` 머리글은 예외입니다. 또한 `was_published_recently`에 대한 열 머리글은 기본적으로 메서드의 이름 (밑줄을 공백으로 바꿈) 이고 각 줄에는 출력의 문자열 표현이 포함되어 있습니다.

`polls/models.py`에서 해당 메서드에 `~django.contrib.admin.display` 데코레이터를 사용하여 이를 개선할 수 있습니다.

```python
from django.contrib import admin


class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

데코레이터를 통해 구성 가능한 속성에 대한 자세한 내용은 `~django.contrib.admin.ModelAdmin.list_display`를 참조하십시오.

`polls/admin.py` 파일을 다시 편집하고 `Question` 변경 목록 페이지에 개선 사항을 추가합니다. `~django.contrib.admin.ModelAdmin.list_filter`를 사용하여 필터를 추가합니다. `QuestionAdmin`에 다음 줄을 추가합니다.

```python
list_filter = ["pub_date"]
```

그러면 사람들이 `pub_date` 필드로 변경 목록을 필터링할 수 있는 "Filter" 사이드바가 추가됩니다.

![Admin list filter sidebar](../assets/20230908-16-16-39-otfMNyYo.png)

표시되는 필터 유형은 필터링하는 필드의 유형에 따라 다릅니다. `pub_date`가 `~django.db.models.DateTimeField`이므로 Django 는 적절한 필터 옵션 ("Any date", "Today", "Past 7 days", "This month", "This year") 을 제공해야 함을 알고 있습니다.

이것은 잘 진행되고 있습니다. 검색 기능을 추가해 보겠습니다.

```python
search_fields = ["question_text"]
```

그러면 변경 목록 상단에 검색 상자가 추가됩니다. 누군가 검색어를 입력하면 Django 는 `question_text` 필드를 검색합니다. 원하는 만큼 많은 필드를 사용할 수 있습니다. 하지만 백그라운드에서 `LIKE` 쿼리를 사용하므로 검색 필드 수를 적절한 수로 제한하면 데이터베이스에서 검색을 더 쉽게 수행할 수 있습니다.

이제 변경 목록에서 무료 페이지 매김을 제공한다는 점도 언급할 때입니다. 기본값은 페이지당 100 개의 항목을 표시하는 것입니다. `Change list pagination
<django.contrib.admin.ModelAdmin.list_per_page>`, `search boxes
<django.contrib.admin.ModelAdmin.search_fields>`, `filters
<django.contrib.admin.ModelAdmin.list_filter>`, `date-hierarchies
<django.contrib.admin.ModelAdmin.date_hierarchy>`, 및 `column-header-ordering <django.contrib.admin.ModelAdmin.list_display>`는 모두 예상대로 함께 작동합니다.
