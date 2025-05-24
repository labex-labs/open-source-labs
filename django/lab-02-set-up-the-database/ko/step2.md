# 모델 생성

이제 모델을 정의합니다. 본질적으로, 추가 메타데이터가 있는 데이터베이스 레이아웃입니다.

모델은 데이터에 대한 단일하고 결정적인 정보 소스입니다. 저장하려는 데이터의 필수 필드와 동작을 포함합니다. Django 는 `DRY 원칙 <dry>`을 따릅니다. 목표는 데이터 모델을 한 곳에서 정의하고 자동으로 파생하는 것입니다.

여기에는 마이그레이션이 포함됩니다. 예를 들어 Ruby On Rails 와 달리, 마이그레이션은 모델 파일에서 완전히 파생되며, Django 가 데이터베이스 스키마를 현재 모델에 맞게 업데이트하기 위해 롤백할 수 있는 기록입니다.

Poll 앱에서 `Question`과 `Choice`의 두 가지 모델을 생성합니다. `Question`에는 질문과 게시 날짜가 있습니다. `Choice`에는 두 개의 필드가 있습니다: 선택 텍스트와 투표 집계입니다. 각 `Choice`는 `Question`과 연결됩니다.

이러한 개념은 Python 클래스로 표현됩니다. `polls/models.py` 파일을 다음과 같이 편집합니다.

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

여기서 각 모델은 `django.db.models.Model`을 서브클래싱하는 클래스로 표현됩니다. 각 모델에는 여러 클래스 변수가 있으며, 각 변수는 모델의 데이터베이스 필드를 나타냅니다.

각 필드는 `~django.db.models.Field` 클래스의 인스턴스로 표현됩니다. 예를 들어, 문자 필드의 경우 `~django.db.models.CharField`이고, 날짜/시간의 경우 `~django.db.models.DateTimeField`입니다. 이것은 Django 에게 각 필드가 어떤 유형의 데이터를 보유하는지 알려줍니다.

각 `~django.db.models.Field` 인스턴스의 이름 (예: `question_text` 또는 `pub_date`) 은 기계 친화적인 형식의 필드 이름입니다. 이 값을 Python 코드에서 사용하며, 데이터베이스는 이를 열 이름으로 사용합니다.

`~django.db.models.Field`에 선택적 첫 번째 위치 인수를 사용하여 사람이 읽을 수 있는 이름을 지정할 수 있습니다. 이는 Django 의 몇 가지 자기 성찰적인 부분에서 사용되며, 문서 역할도 합니다. 이 필드가 제공되지 않으면 Django 는 기계가 읽을 수 있는 이름을 사용합니다. 이 예에서는 `Question.pub_date`에 대해서만 사람이 읽을 수 있는 이름을 정의했습니다. 이 모델의 다른 모든 필드의 경우, 필드의 기계가 읽을 수 있는 이름이 사람이 읽을 수 있는 이름으로 충분합니다.

일부 `~django.db.models.Field` 클래스에는 필수 인수가 있습니다. 예를 들어, `~django.db.models.CharField`는 `~django.db.models.CharField.max_length`를 제공해야 합니다. 이는 데이터베이스 스키마뿐만 아니라 곧 보게 될 유효성 검사에도 사용됩니다.

`~django.db.models.Field`는 다양한 선택적 인수를 가질 수도 있습니다. 이 경우, `votes`의 `~django.db.models.Field.default` 값을 0 으로 설정했습니다.

마지막으로, `~django.db.models.ForeignKey`를 사용하여 관계가 정의되었음을 확인하십시오. 이는 Django 에게 각 `Choice`가 단일 `Question`과 관련되어 있음을 알려줍니다. Django 는 모든 일반적인 데이터베이스 관계를 지원합니다: 다대일, 다대다 및 일대일.
