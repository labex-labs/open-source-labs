# ビューをテストする

`polls` アプリケーションは比較的制限が少なく、未来の `pub_date` フィールドを持つ質問を含む、任意の質問を公開します。これを改善する必要があります。未来の日付を設定することは、その時点で質問が公開されることを意味しますが、それまでは非表示になります。

## ビューのテスト

上記のバグを修正する際、私たちはまずテストを書き、その後修正するコードを書きました。実際、これはテスト駆動開発の例でしたが、作業の順序は実際にはあまり重要ではありません。

最初のテストでは、コードの内部動作に焦点を当てました。このテストでは、ユーザーがウェブブラウザを通じて経験するような動作を確認したいと思います。

何かを修正しようとする前に、利用可能なツールを見てみましょう。

## Django テストクライアント

Django は、ユーザーがビューレベルでコードと対話することをシミュレートするためのテスト用の `~django.test.Client` を提供しています。これを `tests.py` で、あるいは `shell` でも使用できます。

ここでは再び `shell` から始めます。ここでは、`tests.py` では必要ないいくつかのことを行う必要があります。最初のことは、`shell` 内でテスト環境を設定することです：

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` は、レスポンスの一部の追加属性（例えば `response.context`）を調べることができるようにするためのテンプレートレンダラーをインストールします。これらの属性は、そうでなければ利用できません。このメソッドはテストデータベースをセットアップしませんので、以下の操作は既存のデータベースに対して実行され、出力は既に作成した質問によって多少異なる場合があります。`settings.py` 内の `TIME_ZONE` が正しく設定されていない場合、予期しない結果が得られるかもしれません。もし以前に設定したことを忘れている場合は、続ける前に確認してください。

次に、テストクライアントクラスをインポートする必要があります（後で `tests.py` では、独自のクライアントを持つ `django.test.TestCase` クラスを使用するため、これは必要ありません）：

```python
>>> from django.test import Client
>>> # 私たちが使用するためのクライアントのインスタンスを作成
>>> client = Client()
```

これが準備できたら、クライアントにいくつかの作業を依頼できます：

```python
>>> # '/' からレスポンスを取得
>>> response = client.get("/")
Not Found: /
>>> # そのアドレスから 404 が返ることを期待する必要があります。代わりに
>>> # "Invalid HTTP_HOST header" エラーと 400 レスポンスが表示される場合、おそらく
>>> # 前述の setup_test_environment() の呼び出しを省略しています。
>>> response.status_code
404
>>> # 一方、'/polls/' には何かが見つかるはずです
>>> # ハードコードされた URL ではなく'reverse()' を使用します
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## ビューの改善

投票の一覧にはまだ公開されていない投票（すなわち、未来の `pub_date` を持つもの）が表示されています。これを修正しましょう。

`**Form Processing and Cutting Down Our Code**` では、`~django.views.generic.list.ListView` に基づくクラスベースのビューを導入しました：

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
```

`get_queryset()` メソッドを修正して、`timezone.now()` と比較することで日付をチェックするように変更する必要があります。まずインポートを追加する必要があります：

```python
from django.utils import timezone
```

そして、`get_queryset` メソッドを以下のように修正する必要があります：

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

`Question.objects.filter(pub_date__lte=timezone.now())` は、`pub_date` が `timezone.now` 以前（すなわち、以前または等しい）である `Question` を含むクエリセットを返します。

## 新しいビューのテスト

これで、`runserver` を起動してブラウザでサイトを読み込み、過去と未来の日付を持つ `Question` を作成し、公開されたもののみが表示されることを確認することで、これが期待通りに動作することを確認できます。しかし、これを「システムに影響を与える可能性のあるすべての変更を行うたびに」行うのは面倒です。ですから、上記の `shell` セッションに基づいてテストも作成しましょう。

`polls/tests.py` に以下を追加します：

```python
from django.urls import reverse
```

そして、質問を作成するためのショートカット関数と新しいテストクラスを作成します：

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

これらのうちいくつかをもう少し詳しく見てみましょう。

最初は質問のショートカット関数 `create_question` で、質問を作成するプロセスからいくつかの繰り返しを省きます。

`test_no_questions` は質問を作成せずに、メッセージ "No polls are available." をチェックし、`latest_question_list` が空であることを検証します。`django.test.TestCase` クラスはいくつかの追加のアサーションメソッドを提供しています。これらの例では、`~django.test.SimpleTestCase.assertContains()` と `~django.test.TransactionTestCase.assertQuerySetEqual()` を使用しています。

`test_past_question` では、質問を作成してリストに表示されることを検証します。

`test_future_question` では、未来の `pub_date` を持つ質問を作成します。各テストメソッドでデータベースがリセットされるため、最初の質問はもう存在しなくなり、したがってインデックスにはもう質問が表示されないはずです。

その他も同様です。実際、私たちはテストを使って、サイト上の管理者の入力とユーザーの経験の物語を語り、システムの状態のあらゆる状態とその状態のあらゆる新しい変更に対して、期待される結果が表示されることを確認しています。

## `DetailView` のテスト

これまでの作業でうまくいっています。しかし、未来の質問はインデックスには表示されませんが、ユーザーが正しい URL を知っているか、または推測すれば、まだ到達できてしまいます。ですから、`DetailView` にも同様の制約を追加する必要があります：

```python
class DetailView(generic.DetailView):
  ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

その後、過去の `pub_date` を持つ `Question` が表示され、未来の `pub_date` を持つものは表示されないことを確認するためのいくつかのテストを追加する必要があります：

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

## さらに多くのテストのアイデア

`ResultsView` にも同様の `get_queryset` メソッドを追加し、そのビュー用の新しいテストクラスを作成する必要があります。これは、私たちが今作成したものと非常に似ています。実際、多くの繰り返しがあります。

また、他の方法でアプリケーションを改善し、その途中でテストを追加することもできます。たとえば、`Choices` を持たない `Questions` がサイト上に公開されるのは不適切です。ですから、ビューはこれをチェックし、そのような `Questions` を除外することができます。私たちのテストは、`Choices` を持たない `Question` を作成して、それが公開されないことをテストするだけでなく、同様の `Question` を `Choices` とともに作成して、それが公開されることをテストします。

ログインした管理者ユーザーは未公開の `Questions` を見ることができるかもしれませんが、通常の訪問者は見ることができません。再び申しますが、これを達成するためにソフトウェアに追加する必要のあるものは、どれでもテストに付随する必要があります。テストを最初に書いてからコードをテストに合格させるか、または最初にコード内のロジックを考えてからそれを証明するためのテストを書くかは問いません。

ある時点で、あなたは必ずあなたのテストを見て、あなたのコードがテストの肥大化に苦しんでいないかと疑問に思うでしょう。これが私たちに導くものです：
