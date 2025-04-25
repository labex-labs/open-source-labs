# 最初のテストを書く

## バグを特定する

幸いなことに、`polls` アプリケーションにはすぐに修正する必要のある小さなバグがあります。`Question.was_published_recently()` メソッドは、`Question` が過去 1 日以内に公開された場合（これは正しい）に `True` を返しますが、`Question` の `pub_date` フィールドが未来の場合も `True` を返します（これは明らかに正しくありません）。

未来の日付を持つ質問に対するメソッドを `shell` を使って確認することで、このバグを確認しましょう：

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # 未来 30 日後の pub_date を持つ Question インスタンスを作成
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # 最近公開されましたか？
>>> future_question.was_published_recently()
True
```

未来のものは「最近」ではないので、これは明らかに間違っています。

## バグを明らかにするためのテストを作成する

問題をテストするために `shell` で先ほど行ったことは、自動テストでもまったく同じことができます。では、それを自動テストに変換しましょう。

アプリケーションのテストの一般的な場所は、アプリケーションの `tests.py` ファイルです。テストシステムは、`test` で始まる名前の任意のファイル内のテストを自動的に見つけます。

`polls` アプリケーションの `tests.py` ファイルに以下を記述します：

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() は、pub_date が未来の質問に対して False を返します。
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

ここでは、`django.test.TestCase` サブクラスを作成し、そのメソッドで未来の `pub_date` を持つ `Question` インスタンスを作成しています。その後、`was_published_recently()` の出力を確認します。これは `False` であるはずです。

## テストを実行する

ターミナルでテストを実行します：

```bash
python manage.py test polls
```

すると、以下のような出力が表示されます：

```shell
[object Object]
```

> 異なるエラーが表示されますか？

ここで `NameError` が表示される場合は、`Part 2 <tutorial02-import-timezone>` の手順を抜けている可能性があります。そこでは、`polls/models.py` に `datetime` と `timezone` のインポートを追加しました。そのセクションのインポートをコピーして、再度テストを実行してみてください。

以下のようになります：

- `manage.py test polls` は `polls` アプリケーション内のテストを探します。
- `django.test.TestCase` クラスのサブクラスを見つけます。
- テスト用に特別なデータベースを作成します。
- テストメソッド（`test` で始まる名前のもの）を探します。
- `test_was_published_recently_with_future_question` では、`pub_date` フィールドが未来 30 日後の `Question` インスタンスを作成します。
- `assertIs()` メソッドを使って、`was_published_recently()` が `True` を返すことを発見しました。ただし、私たちは `False` を返すことを望んでいました。

テストは、どのテストが失敗したか、さらには失敗が発生した行までを通知します。

## バグを修正する

既に問題が何であるかはわかっています。`Question.was_published_recently()` は、`pub_date` が未来の場合には `False` を返すようにする必要があります。`models.py` のメソッドを修正して、日付が過去の場合のみ `True` を返すようにします：

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

そして、再度テストを実行します：

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

バグを特定した後、それを明らかにするテストを書き、コード内のバグを修正してテストが通過するようにしました。

これから、アプリケーションで他の多くのことがうまくいかなくなるかもしれませんが、このバグを無注意に再現することはないことが確信できます。なぜなら、テストを実行するとすぐに警告が表示されるからです。このアプリケーションのこの小さな部分は、永遠に安全に固定された状態になっていると考えることができます。

## より包括的なテスト

ここで、`was_published_recently()` メソッドをさらに固定することができます。実際、1 つのバグを修正した際に別のバグを導入してしまったら恥ずかしいことになります。

同じクラスにさらに 2 つのテストメソッドを追加して、メソッドの動作をより包括的にテストします：

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() は、pub_date が 1 日以上前の質問に対して False を返します。
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() は、pub_date が過去 1 日以内の質問に対して True を返します。
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

そして今、`Question.was_published_recently()` が過去、最近、未来の質問に対して適切な値を返すことを確認する 3 つのテストがあります。

再び申しますが、`polls` は最小限のアプリケーションですが、これからどんなに複雑になっても、他のどのコードと相互作用しても、テストを書いたメソッドが期待通りに動作することが保証されています。
