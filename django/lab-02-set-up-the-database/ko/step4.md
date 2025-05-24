# API 사용해보기

이제 대화형 Python 셸에 들어가 Django 가 제공하는 무료 API 를 사용해 보겠습니다. Python 셸을 호출하려면 다음 명령을 사용하십시오.

```bash
python manage.py shell
```

"python"을 단순히 입력하는 대신 이것을 사용하고 있습니다. `manage.py`는 `DJANGO_SETTINGS_MODULE` 환경 변수를 설정하여 Django 에게 `mysite/settings.py` 파일에 대한 Python import 경로를 제공합니다.

셸에 들어가면 `database API </topics/db/queries>`를 탐색하십시오.

```python
>>> from polls.models import Choice, Question  # 방금 작성한 모델 클래스를 가져옵니다.

# 아직 시스템에 질문이 없습니다.
>>> Question.objects.all()
<QuerySet []>

# 새 질문을 만듭니다.
# 기본 설정 파일에서 시간대 지원이 활성화되어 있으므로
# Django 는 pub_date 에 tzinfo 가 있는 datetime 을 예상합니다. datetime.datetime.now() 대신 timezone.now() 를 사용하면
# 올바르게 작동합니다.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# 객체를 데이터베이스에 저장합니다. save() 를 명시적으로 호출해야 합니다.
>>> q.save()

# 이제 ID 가 있습니다.
>>> q.id
1

# Python 속성을 통해 모델 필드 값에 액세스합니다.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# 속성을 변경한 다음 save() 를 호출하여 값을 변경합니다.
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() 은 데이터베이스의 모든 질문을 표시합니다.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

잠깐만요. `<Question: Question object (1)>`은 이 객체의 유용한 표현이 아닙니다. `Question` 모델 ( `polls/models.py` 파일) 을 편집하고 `Question`과 `Choice` 모두에 `~django.db.models.Model.__str__` 메서드를 추가하여 이를 수정해 보겠습니다.

```python
from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

대화형 프롬프트를 처리할 때뿐만 아니라 객체의 표현이 Django 의 자동 생성된 관리자 전체에서 사용되기 때문에 모델에 `~django.db.models.Model.__str__` 메서드를 추가하는 것이 중요합니다.

이 모델에 사용자 지정 메서드도 추가해 보겠습니다.

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Python 의 표준 `datetime` 모듈과 Django 의 시간대 관련 유틸리티를 각각 `django.utils.timezone`에서 참조하기 위해 `import datetime` 및 `from django.utils import timezone`이 추가된 것을 확인하십시오. Python 에서 시간대 처리에 익숙하지 않은 경우, `time zone support docs </topics/i18n/timezones>`에서 자세한 내용을 확인할 수 있습니다.

이러한 변경 사항을 저장하고 **`python manage.py shell`을 다시 실행하여** 새 Python 대화형 셸을 시작합니다.

```python
>>> from polls.models import Choice, Question

# __str__() 추가가 작동하는지 확인합니다.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django 는 키워드 인수로 완전히 구동되는 풍부한 데이터베이스 조회 API 를 제공합니다.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# 올해 게시된 질문을 가져옵니다.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# 존재하지 않는 ID 를 요청하면 예외가 발생합니다.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# 기본 키로 조회가 가장 일반적인 경우이므로 Django 는 기본 키 정확 조회를 위한 바로 가기를 제공합니다.
# 다음은 Question.objects.get(id=1) 과 동일합니다.
>>> Question.objects.get(pk=1)
<Question: What's up?>

# 사용자 지정 메서드가 작동하는지 확인합니다.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Question 에 몇 가지 Choice 를 제공합니다. create 호출은 새
# Choice 객체를 구성하고, INSERT 문을 실행하고, 선택 항목을
# 사용 가능한 선택 항목 집합에 추가하고 새 Choice 객체를 반환합니다. Django 는
# ForeignKey 관계의 "다른 쪽"(예: 질문의 선택) 을 보유할 집합을 만듭니다.
# API 를 통해 액세스할 수 있습니다.
>>> q = Question.objects.get(pk=1)

# 관련 객체 집합의 선택 항목을 표시합니다. 아직 없습니다.
>>> q.choice_set.all()
<QuerySet []>

# 세 가지 선택 항목을 만듭니다.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice 객체는 관련 Question 객체에 대한 API 액세스 권한을 갖습니다.
>>> c.question
<Question: What's up?>

# 그리고 그 반대도 마찬가지입니다. Question 객체는 Choice 객체에 대한 액세스 권한을 얻습니다.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# API 는 필요에 따라 관계를 자동으로 따릅니다.
# 관계를 구분하려면 밑줄 두 개를 사용합니다.
# 이것은 원하는 만큼 여러 수준에서 작동합니다. 제한이 없습니다.
# pub_date 가 올해인 질문에 대한 모든 Choice 를 찾습니다.
# (위에서 만든 'current_year' 변수를 재사용합니다).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# 선택 항목 중 하나를 삭제해 보겠습니다. delete() 를 사용합니다.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

모델 관계에 대한 자세한 내용은 `Accessing related objects
</ref/models/relations>`를 참조하십시오. API를 통해 필드 조회를 수행하기 위해 밑줄 두 개를 사용하는 방법에 대한 자세한 내용은 `Field lookups <field-lookups-intro>`를 참조하십시오. 데이터베이스 API에 대한 자세한 내용은 `Database API reference
</topics/db/queries>`를 참조하십시오.
