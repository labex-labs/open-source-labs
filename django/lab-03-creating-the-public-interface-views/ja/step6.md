# テンプレート内のハードコードされた URL を削除する

覚えていますか？`polls/index.html` テンプレート内の質問へのリンクを書いたとき、リンクは次のように部分的にハードコードされていました。

```html+django
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

このハードコードされた密結合のアプローチの問題は、多くのテンプレートがあるプロジェクトで URL を変更するのが難しくなることです。ただし、`polls.urls` モジュールの `~django.urls.path` 関数で名前引数を定義したので、`{% url %}` テンプレートタグを使用することで、URL 設定で定義された特定の URL パスに対する依存を排除することができます。

```html+django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

この機能は、`polls.urls` モジュールで指定された URL 定義を参照することによって機能します。`detail` という URL 名がどこで定義されているかを正確に見ることができます。以下に示します。

```python
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
```

投票の詳細ビューの URL を別のものに変更したい場合、たとえば `polls/specifics/12/` のようなものに変更したい場合は、テンプレート（または複数のテンプレート）で行うのではなく、`polls/urls.py` で変更します。

> テンプレート自体をまったく変更する必要はありません。

```python
# added the word'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```
