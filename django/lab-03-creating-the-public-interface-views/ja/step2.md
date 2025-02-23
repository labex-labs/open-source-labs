# さらに多くのビューを作成する

では、`polls/views.py` にいくつかのビューを追加しましょう。これらのビューは少し異なります。引数を取るからです。

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

次の `~django.urls.path` 呼び出しを追加することで、これらの新しいビューを `polls.urls` モジュールに接続します。

`polls/urls.py` ファイルを編集して、次の行を追加します。

```python
from django.urls import path

from. import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

次に、サーバーを再度起動します。

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

**Web 8080** タブに切り替えて、`/polls/34/` にアクセスします。`detail()` メソッドが実行され、URLに提供したIDが表示されます。`/polls/34/results/` と `/polls/34/vote/` も試してみてください。これらは、仮の結果と投票ページを表示します。

![Django URL routing diagram](../assets/20230908-09-30-06-2n54ROPe.png)

誰かがあなたのウェブサイトからページを要求するとき、たとえば `/polls/34/` の場合、Djangoは `ROOT_URLCONF` 設定によって指定されているため、`mysite.urls` Pythonモジュールを読み込みます。`urlpatterns` という名前の変数を見つけ、順番にパターンを辿ります。`'polls/'` で一致するものを見つけた後、一致するテキスト（`"polls/"`）を取り除き、残りのテキスト（`"34/"`）を 'polls.urls' URLconfに送り、さらに処理します。そこでは `'<int:question_id>/'` と一致し、次のように `detail()` ビューが呼び出されます。

```python
detail(request=<HttpRequest object>, question_id=34)
```

`question_id=34` の部分は `<int:question_id>` から来ています。角括弧を使うことで、URLの一部を「キャプチャ」し、ビュー関数にキーワード引数として渡します。文字列の `question_id` の部分は、一致したパターンを識別するために使用される名前を定義し、`int` の部分は、URLパスのこの部分に一致するパターンを決定するコンバーターです。コロン（`:`）はコンバーターとパターン名を区切ります。
