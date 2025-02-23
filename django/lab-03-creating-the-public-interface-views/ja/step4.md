# 404エラーを発生させる

では、質問の詳細ビューを取り扱いましょう。このビューは、特定の投票に対する質問文を表示するページです。以下がそのビューです。

```python
from django.http import Http404
from django.shortcuts import render

from.models import Question


#...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

ここでの新しい概念は、要求されたIDの質問が存在しない場合、ビューが `~django.http.Http404` 例外を発生させることです。

後で `polls/detail.html` テンプレートに何を入れるかについて説明しますが、すぐに上記の例を動作させたい場合は、ただ次の内容のファイルがあれば始めることができます。

```html+django
{{ question }}
```

## ショートカット: `~django.shortcuts.get_object_or_404`

`~django.db.models.query.QuerySet.get` を使用し、オブジェクトが存在しない場合に `~django.http.Http404` を発生させるのは、非常に一般的な慣用句です。Djangoはショートカットを提供しています。以下が書き直された `detail()` ビューです。

```python
from django.shortcuts import get_object_or_404, render

from.models import Question


#...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

`~django.shortcuts.get_object_or_404` 関数は、最初の引数にDjangoモデルを取り、任意の数のキーワード引数を取り、それらをモデルのマネージャーの `~django.db.models.query.QuerySet.get` 関数に渡します。オブジェクトが存在しない場合、`~django.http.Http404` を発生させます。

なぜ、ヘルパー関数 `~django.shortcuts.get_object_or_404` を使って、より上位のレベルで `~django.core.exceptions.ObjectDoesNotExist` 例外を自動的にキャッチしたり、モデルAPIが `~django.http.Http404` を `~django.core.exceptions.ObjectDoesNotExist` の代わりに発生させたりしないのでしょうか？

それは、モデル層をビュー層に結合させてしまうからです。Djangoの最も重要な設計目標の1つは、緩やかな結合を維持することです。`django.shortcuts` モジュールには、いくつかの制御された結合が導入されています。

`~django.shortcuts.get_list_or_404` 関数もあります。これは `~django.shortcuts.get_object_or_404` と同じように機能しますが、`~django.db.models.query.QuerySet.get` の代わりに `~django.db.models.query.QuerySet.filter` を使用します。リストが空の場合、`~django.http.Http404` を発生させます。
