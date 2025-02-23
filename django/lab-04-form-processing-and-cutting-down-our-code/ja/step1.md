# 最小限のフォームを作成する

前回のチュートリアルで作成した投票詳細テンプレート（`polls/detail.html`）を更新しましょう。このテンプレートにHTMLの`<form>`要素を含めます。

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

簡単な説明：

- 上記のテンプレートは、各質問の選択肢に対してラジオボタンを表示します。各ラジオボタンの`value`は、関連する質問の選択肢のIDです。各ラジオボタンの`name`は`"choice"`です。つまり、誰かがラジオボタンの1つを選択してフォームを送信すると、POSTデータ`choice=#`が送信されます。ここで`#`は選択された選択肢のIDです。これがHTMLフォームの基本的な概念です。
- フォームの`action`を`{% url 'polls:vote' question.id %}`に設定し、`method="post"`に設定しました。`method="post"`（`method="get"`とは対照的）を使用することは非常に重要です。なぜなら、このフォームを送信するとサーバーサイドのデータが変更されるからです。サーバーサイドのデータを変更するフォームを作成する場合は常に`method="post"`を使用します。このヒントはDjangoに特有のものではありません。一般的な良いウェブ開発の慣習です。
- `forloop.counter`は、`for`タグがループを何回行ったかを示します。
- 私たちが作成しているのはPOSTフォーム（データを変更する可能性がある）なので、クロスサイトリクエスト偽装について心配する必要があります。幸いなことに、あまり苦労する必要はありません。なぜなら、Djangoには対策するための便利なシステムが備えているからです。要するに、内部URLを対象とするすべてのPOSTフォームは、`{% csrf_token %}<csrf_token>`テンプレートタグを使用する必要があります。

では、送信されたデータを処理して何かを行うDjangoのビューを作成しましょう。覚えておいてください。`**パブリックインターフェイスビューの作成**`では、投票アプリケーション用のURLconfを作成しました。このURLconfには次の行が含まれています。

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

また、`vote()`関数のダミー実装も作成しました。本物のバージョンを作成しましょう。`polls/views.py`に次のコードを追加します。

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from.models import Choice, Question


#...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # 質問の投票フォームを再表示します。
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POSTデータを正常に処理した後は常にHttpResponseRedirectを返します。
        # これにより、ユーザーが戻るボタンを押した場合にデータが2回送信されるのを防ぎます。
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

このコードには、このチュートリアルでまだ扱っていないいくつかの要素が含まれています。

- `request.POST <django.http.HttpRequest.POST>`は、キー名で送信されたデータにアクセスできる辞書のようなオブジェクトです。この場合、`request.POST['choice']`は選択された選択肢のIDを文字列として返します。`request.POST <django.http.HttpRequest.POST>`の値は常に文字列です。

  ただし、Djangoは同じ方法でGETデータにアクセスするための`request.GET
<django.http.HttpRequest.GET>`も提供しています。ただし、私たちはコードで明示的に`request.POST
<django.http.HttpRequest.POST>`を使用しています。これにより、データがPOST呼び出しを介してのみ変更されることを確認します。

- `request.POST['choice']`は、POSTデータに`choice`が提供されていない場合に`KeyError`を発生させます。上記のコードは`KeyError`をチェックし、`choice`が指定されていない場合にエラーメッセージ付きで質問フォームを再表示します。
- 選択肢のカウントを増やした後、コードは通常の`~django.http.HttpResponse`ではなく`~django.http.HttpResponseRedirect`を返します。`~django.http.HttpResponseRedirect`は1つの引数を取ります。この引数は、ユーザーがリダイレクトされるURLです（この場合、URLを構築する方法については次の項を参照）。

  上のPythonのコメントにもあるように、POSTデータを正常に処理した後は常に`~django.http.HttpResponseRedirect`を返す必要があります。このヒントはDjangoに特有のものではありません。一般的な良いウェブ開発の慣習です。

- この例では、`~django.http.HttpResponseRedirect`コンストラクタで`~django.urls.reverse`関数を使用しています。この関数は、ビュー関数でURLをハードコードする必要を回避するのに役立ちます。これには、制御を渡したいビューの名前と、そのビューを指すURLパターンの可変部分が与えられます。この場合、`**パブリックインターフェイスビューの作成**`で設定したURLconfを使用すると、この`~django.urls.reverse`呼び出しは次のような文字列を返します。

      "/polls/3/results/"

  ここで`3`は`question.id`の値です。このリダイレクトされたURLは、最終的なページを表示するために`'results'`ビューを呼び出します。

`**パブリックインターフェイスビューの作成**`で述べたように、`request`は`~django.http.HttpRequest`オブジェクトです。`~django.http.HttpRequest`オブジェクトに関する詳細については、`request and
response documentation </ref/request-response>`を参照してください。

誰かが質問に投票した後、`vote()`ビューは質問の結果ページにリダイレクトします。そのビューを書きましょう。

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

これは、`**パブリックインターフェイスビューの作成**`の`detail()`ビューとほぼ同じです。唯一の違いはテンプレート名です。後でこの冗長性を修正します。

では、`polls/results.html`テンプレートを作成しましょう。

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

では、ブラウザで`/polls/1/`に移動して質問に投票してみましょう。投票するたびに結果ページが更新されるはずです。選択肢を選ばずにフォームを送信すると、エラーメッセージが表示されるはずです。

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![投票フォームインターフェイス](../assets/20230908-10-37-07-p9ewKbe6.png)

**注記**：

私たちの`vote()`ビューのコードには小さな問題があります。まず、データベースから`selected_choice`オブジェクトを取得し、次に`votes`の新しい値を計算し、そしてそれをデータベースに保存します。あなたのウェブサイトの2人のユーザーがまさに同時に投票しようとした場合、これがうまくいかないことがあります。同じ値、たとえば42が`votes`として取得されます。そして、両方のユーザーにとって新しい値43が計算されて保存されますが、期待される値は44です。

これは「競合条件」と呼ばれます。興味があれば、`avoiding-race-conditions-using-f`を読んで、この問題をどのように解決するか学ぶことができます。
