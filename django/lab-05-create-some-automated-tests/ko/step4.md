# 뷰 테스트

polls 애플리케이션은 상당히 무차별적입니다. `pub_date` 필드가 미래에 있는 질문을 포함하여 모든 질문을 게시합니다. 이를 개선해야 합니다. 미래에 `pub_date`를 설정하는 것은 해당 시점에 질문이 게시되지만, 그 전까지는 보이지 않음을 의미해야 합니다.

## 뷰에 대한 테스트

위에서 버그를 수정했을 때, 우리는 먼저 테스트를 작성한 다음, 이를 수정하는 코드를 작성했습니다. 사실 그것은 테스트 주도 개발의 예였지만, 우리가 작업을 어떤 순서로 하든 실제로 중요하지 않습니다.

첫 번째 테스트에서는 코드의 내부 동작에 집중했습니다. 이 테스트에서는 웹 브라우저를 통해 사용자가 경험하는 것처럼 동작을 확인하려고 합니다.

무언가를 수정하기 전에, 우리가 사용할 수 있는 도구를 살펴보겠습니다.

## Django 테스트 클라이언트

Django 는 뷰 수준에서 코드와 상호 작용하는 사용자를 시뮬레이션하기 위해 테스트 `~django.test.Client`를 제공합니다. `tests.py` 또는 심지어 `shell`에서도 사용할 수 있습니다.

`shell`에서 다시 시작합니다. 여기서는 `tests.py`에서 필요하지 않은 몇 가지 작업을 수행해야 합니다. 첫 번째는 `shell`에서 테스트 환경을 설정하는 것입니다.

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment`는 응답에서 `response.context`와 같이 그렇지 않으면 사용할 수 없는 몇 가지 추가 속성을 검사할 수 있도록 템플릿 렌더러를 설치합니다. 이 메서드는 _테스트 데이터베이스를 설정하지 않으므로_, 다음은 기존 데이터베이스에 대해 실행되며 이미 생성한 질문에 따라 출력이 약간 다를 수 있습니다. `settings.py`의 `TIME_ZONE`이 올바르지 않으면 예기치 않은 결과가 발생할 수 있습니다. 이전에 설정했는지 기억나지 않으면, 계속하기 전에 확인하십시오.

다음으로 테스트 클라이언트 클래스를 가져와야 합니다 (나중에 `tests.py`에서는 자체 클라이언트가 있는 `django.test.TestCase` 클래스를 사용하므로, 이것은 필요하지 않습니다).

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

준비가 되면, 클라이언트에게 몇 가지 작업을 요청할 수 있습니다.

```python
>>> # get a response from '/'
>>> response = client.get("/")
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## 뷰 개선

polls 목록은 아직 게시되지 않은 polls(즉, `pub_date`가 미래에 있는 polls) 를 표시합니다. 이를 수정해 보겠습니다.

`**Form Processing and Cutting Down Our Code**`에서 `~django.views.generic.list.ListView`를 기반으로 하는 클래스 기반 뷰를 소개했습니다.

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
```

`get_queryset()` 메서드를 수정하고 `timezone.now()`와 비교하여 날짜도 확인하도록 변경해야 합니다. 먼저 import 를 추가해야 합니다.

```python
from django.utils import timezone
```

그런 다음 다음과 같이 `get_queryset` 메서드를 수정해야 합니다.

```python
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```

`Question.objects.filter(pub_date__lte=timezone.now())`는 `pub_date`가 `timezone.now`보다 작거나 같은 (즉, 이전이거나 같은) `Question`을 포함하는 쿼리셋을 반환합니다.

## 새로운 뷰 테스트

이제 `runserver`를 시작하고, 브라우저에서 사이트를 로드하고, 과거와 미래의 날짜로 `Question`을 생성하고, 게시된 질문만 나열되는지 확인하여 예상대로 동작하는지 확인할 수 있습니다. _이것에 영향을 미칠 수 있는 변경을 할 때마다_ 매번 그렇게 할 필요는 없으므로, 위의 `shell` 세션을 기반으로 테스트도 만들어 보겠습니다.

`polls/tests.py`에 다음을 추가합니다.

```python
from django.urls import reverse
```

그리고 질문을 생성하는 바로 가기 함수와 새로운 테스트 클래스를 만들겠습니다.

```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```

이 중 일부를 자세히 살펴보겠습니다.

먼저, 질문을 생성하는 프로세스에서 반복을 제거하기 위한 질문 바로 가기 함수인 `create_question`입니다.

`test_no_questions`는 질문을 생성하지 않지만, "No polls are available." 메시지를 확인하고 `latest_question_list`가 비어 있는지 확인합니다. `django.test.TestCase` 클래스는 몇 가지 추가적인 assertion 메서드를 제공합니다. 이 예제에서는 `~django.test.SimpleTestCase.assertContains()` 및 `~django.test.TransactionTestCase.assertQuerySetEqual()`을 사용합니다.

`test_past_question`에서는 질문을 생성하고 목록에 나타나는지 확인합니다.

`test_future_question`에서는 미래의 `pub_date`를 가진 질문을 생성합니다. 데이터베이스는 각 테스트 메서드마다 재설정되므로, 첫 번째 질문은 더 이상 존재하지 않으며, 따라서 인덱스에도 질문이 없어야 합니다.

등등. 실제로, 우리는 테스트를 사용하여 사이트의 관리자 입력 및 사용자 경험에 대한 이야기를 전달하고, 시스템의 각 상태와 상태의 모든 새로운 변경에 대해 예상되는 결과가 게시되는지 확인하고 있습니다.

## `DetailView` 테스트

우리가 한 일은 잘 작동합니다. 그러나 미래의 질문이 *index*에 나타나지 않더라도, 사용자는 올바른 URL 을 알고 있거나 추측하면 여전히 해당 질문에 도달할 수 있습니다. 따라서 `DetailView`에 유사한 제약 조건을 추가해야 합니다.

```python
class DetailView(generic.DetailView):
    ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

그런 다음, `pub_date`가 과거에 있는 `Question`이 표시될 수 있고, 미래에 있는 `Question`은 표시되지 않는지 확인하기 위해 몇 가지 테스트를 추가해야 합니다.

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## 더 많은 테스트를 위한 아이디어

`ResultsView`에 유사한 `get_queryset` 메서드를 추가하고 해당 뷰에 대한 새로운 테스트 클래스를 만들어야 합니다. 방금 생성한 것과 매우 유사할 것입니다. 사실, 많은 반복이 있을 것입니다.

또한, 그 과정에서 테스트를 추가하여 애플리케이션을 다른 방식으로 개선할 수 있습니다. 예를 들어, `Choices`가 없는 `Questions`가 사이트에 게시될 수 있다는 것은 어리석습니다. 따라서, 우리의 뷰는 이것을 확인하고, 그러한 `Questions`를 제외할 수 있습니다. 우리의 테스트는 `Choices`가 없는 `Question`을 생성한 다음, 게시되지 않는지 테스트하고, 유사한 `Question`을 _with_ `Choices`로 생성하고, 게시되는지 테스트합니다.

아마도 로그인한 관리자 사용자는 게시되지 않은 `Questions`를 볼 수 있지만, 일반 방문자는 볼 수 없어야 합니다. 다시 말하지만, 이를 달성하기 위해 소프트웨어에 추가해야 하는 모든 것은 테스트와 함께 제공되어야 합니다. 테스트를 먼저 작성한 다음, 코드가 테스트를 통과하도록 하거나, 먼저 코드에서 로직을 파악한 다음, 이를 증명하기 위해 테스트를 작성합니다.

특정 시점에서 당신은 당신의 테스트를 보고 당신의 코드가 테스트 과다로 고통받고 있는지 궁금해할 것입니다. 이는 우리를 다음으로 이끕니다.
