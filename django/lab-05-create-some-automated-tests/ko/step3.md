# 첫 번째 테스트 작성

## 버그를 식별합니다.

다행히, `polls` 애플리케이션에 바로 수정할 수 있는 작은 버그가 있습니다. `Question.was_published_recently()` 메서드는 `Question`이 지난 하루 이내에 게시된 경우 (정확함) 와 `Question`의 `pub_date` 필드가 미래에 있는 경우 (확실히 그렇지 않음) 모두 `True`를 반환합니다.

`shell`을 사용하여 날짜가 미래에 있는 질문에 대한 메서드를 확인하여 버그를 확인합니다.

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
```

미래의 것은 '최근'이 아니므로, 이는 명백히 잘못된 것입니다.

## 버그를 노출하는 테스트 생성

문제에 대해 테스트하기 위해 `shell`에서 방금 수행한 작업은 자동화된 테스트에서 수행할 수 있는 정확한 작업이므로, 이를 자동화된 테스트로 바꿔보겠습니다.

애플리케이션 테스트를 위한 일반적인 위치는 애플리케이션의 `tests.py` 파일입니다. 테스트 시스템은 이름이 `test`로 시작하는 모든 파일에서 테스트를 자동으로 찾습니다.

`polls` 애플리케이션의 `tests.py` 파일에 다음을 입력합니다.

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

여기서는 미래의 `pub_date`를 가진 `Question` 인스턴스를 생성하는 메서드가 있는 `django.test.TestCase` 서브클래스를 만들었습니다. 그런 다음 `was_published_recently()`의 출력을 확인합니다. 이는 `False`여야 합니다.

## 테스트 실행

터미널에서 테스트를 실행할 수 있습니다.

```bash
python manage.py test polls
```

다음과 같은 내용이 표시됩니다.

```shell
[object Object]
```

> 다른 오류가 발생했나요?

여기서 `NameError`가 발생한다면, `Part 2 <tutorial02-import-timezone>`에서 `datetime` 및 `timezone`의 import 를 `polls/models.py`에 추가하는 단계를 놓쳤을 수 있습니다. 해당 섹션에서 import 를 복사하여 테스트를 다시 실행해 보세요.

발생한 일은 다음과 같습니다.

- `manage.py test polls`는 `polls` 애플리케이션에서 테스트를 찾았습니다.
- `django.test.TestCase` 클래스의 서브클래스를 찾았습니다.
- 테스트 목적으로 특별한 데이터베이스를 생성했습니다.
- 테스트 메서드 (이름이 `test`로 시작하는 메서드) 를 찾았습니다.
- `test_was_published_recently_with_future_question`에서 `pub_date` 필드가 30 일 후인 `Question` 인스턴스를 생성했습니다.
- ... 그리고 `assertIs()` 메서드를 사용하여 `was_published_recently()`가 `True`를 반환한다는 것을 발견했습니다. 하지만 `False`를 반환하기를 원했습니다.

테스트는 어떤 테스트가 실패했는지, 심지어 실패가 발생한 줄까지 알려줍니다.

## 버그 수정

우리는 이미 문제가 무엇인지 알고 있습니다. `Question.was_published_recently()`는 `pub_date`가 미래에 있는 경우 `False`를 반환해야 합니다. `models.py`에서 메서드를 수정하여 날짜가 과거에 있는 경우에만 `True`를 반환하도록 합니다.

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

그리고 테스트를 다시 실행합니다.

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

버그를 식별한 후, 이를 노출하는 테스트를 작성하고 테스트가 통과하도록 코드의 버그를 수정했습니다.

미래에 우리 애플리케이션에서 다른 많은 문제가 발생할 수 있지만, 이 버그를 실수로 다시 도입하지 않을 수 있습니다. 테스트를 실행하면 즉시 경고를 받기 때문입니다. 우리는 이 애플리케이션의 작은 부분을 영원히 안전하게 고정했다고 간주할 수 있습니다.

## 더 포괄적인 테스트

여기서 우리는 `was_published_recently()` 메서드를 더욱 확실하게 고정할 수 있습니다. 사실, 하나의 버그를 수정하면서 다른 버그를 도입했다면 매우 당황스러울 것입니다.

동일한 클래스에 두 개의 테스트 메서드를 더 추가하여 메서드의 동작을 더욱 포괄적으로 테스트합니다.

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

이제 `Question.was_published_recently()`가 과거, 최근, 미래의 질문에 대해 합리적인 값을 반환하는지 확인하는 세 개의 테스트가 있습니다.

다시 말하지만, `polls`는 최소한의 애플리케이션이지만, 미래에 얼마나 복잡해지든, 다른 코드와 상호 작용하든, 이제 테스트한 메서드가 예상대로 동작한다는 보장을 어느 정도 갖게 되었습니다.
