# テンプレートシステムを使用する

投票アプリケーションの `detail()` ビューに戻りましょう。コンテキスト変数 `question` が与えられた場合、`polls/detail.html` テンプレートは次のようになるかもしれません。

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

テンプレートシステムは、変数の属性にアクセスするためにドット検索構文を使用します。`{{ question.question_text }}` の例では、まず Django はオブジェクト `question` の辞書検索を行います。それが失敗した場合、属性検索を試みます。この場合、それは機能します。属性検索が失敗した場合、リストインデックス検索を試みるでしょう。

メソッド呼び出しは `{% for %}<for>` ループで行われます。`question.choice_set.all` は、Python コード `question.choice_set.all()` として解釈され、`Choice` オブジェクトの反復可能オブジェクトを返し、`{% for %}<for>` タグで使用するのに適しています。
