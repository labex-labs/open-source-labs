# 汎用ビューを使う：コードが少ない方が良い

`detail()`（`**パブリックインターフェイスビューの作成**`から）と`results()`ビューは非常に短く、上記のように冗長です。投票一覧を表示する`index()`ビューも同様です。

これらのビューは、基本的なウェブ開発の一般的なケースを表しています。URL に渡されたパラメータに基づいてデータベースからデータを取得し、テンプレートを読み込み、レンダリングされたテンプレートを返すというものです。これは非常に一般的なため、Django は「汎用ビュー」システムと呼ばれるショートカットを提供しています。

汎用ビューは、共通のパターンを抽象化しており、アプリを書くために Python コードさえ書かなくても良いほどまでです。

投票アプリを汎用ビューシステムを使うように変更しましょう。そうすることで、自分たちのコードをたくさん削除できます。変更にはいくつかの手順が必要です。

1. URLconf を変更する。
2. 古くて不要なビューの一部を削除する。
3. Django の汎用ビューに基づいた新しいビューを導入する。

詳細は以下を読んでください。

> なぜコードを入れ替えるのか？

一般的に、Django アプリを書く際は、汎用ビューが問題に適しているかどうかを評価し、最初から使うようにします。途中でコードをリファクタリングすることはありません。しかし、このチュートリアルではこれまでコアコンセプトに焦点を当てるため、「難しい方法」でビューを書くことに重点を置いてきました。

電卓を使い始める前に基本的な数学を知っておく必要があります。

## URLconf を修正する

まず、`polls/urls.py`の URLconf を開き、以下のように変更します。

```python
from django.urls import path

from. import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

2 番目と 3 番目のパターンのパス文字列での一致するパターンの名前が、`<question_id>`から`<pk>`に変更されていることに注意してください。

## ビューを修正する

次に、古い`index`、`detail`、`results`ビューを削除し、代わりに Django の汎用ビューを使います。そのために、`polls/views.py`ファイルを開き、以下のように変更します。

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from.models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
  ...  # 上と同じで、変更は不要。
```

ここでは 2 つの汎用ビューを使っています。`~django.views.generic.list.ListView`と`~django.views.generic.detail.DetailView`です。それぞれのビューは、「オブジェクトの一覧を表示する」と「特定の種類のオブジェクトの詳細ページを表示する」という概念を抽象化しています。

- 各汎用ビューは、どのモデルに対して動作するかを知る必要があります。これは`model`属性を使って提供されます。
- `~django.views.generic.detail.DetailView`汎用ビューは、URL からキャプチャされた主キー値が`"pk"`と呼ばれることを期待しています。そのため、汎用ビュー用に`question_id`を`pk`に変更しました。

デフォルトでは、`~django.views.generic.detail.DetailView`汎用ビューは`<アプリ名>/<モデル名>_detail.html`と呼ばれるテンプレートを使用します。私たちの場合、`"polls/question_detail.html"`を使用します。`template_name`属性は、Django に自動生成されたデフォルトのテンプレート名の代わりに特定のテンプレート名を使用するように指示するために使用されます。また、`results`一覧ビューの`template_name`も指定しています。これにより、結果ビューと詳細ビューがレンダリングされる際に異なる外見を持つようになります。実際には、両方とも背後で`~django.views.generic.detail.DetailView`です。

同様に、`~django.views.generic.list.ListView`汎用ビューは、`<アプリ名>/<モデル名>_list.html`と呼ばれるデフォルトのテンプレートを使用します。私たちは`template_name`を使って、`~django.views.generic.list.ListView`に既存の`"polls/index.html"`テンプレートを使用するように指示しています。

このチュートリアルの前の部分では、テンプレートには`question`と`latest_question_list`のコンテキスト変数が含まれるコンテキストが提供されていました。`DetailView`の場合、`question`変数は自動的に提供されます。Django モデル（`Question`）を使用しているため、Django はコンテキスト変数に適切な名前を決定できます。一方、`ListView`の場合、自動生成されるコンテキスト変数は`question_list`です。これをオーバーライドするために、`context_object_name`属性を提供して、`latest_question_list`を代わりに使用することを指定しています。別の方法として、新しいデフォルトのコンテキスト変数に合わせてテンプレートを変更することもできます。しかし、Django に使用したい変数を指定する方がはるかに簡単です。

サーバーを起動して、汎用ビューに基づく新しい投票アプリを使ってみましょう。
