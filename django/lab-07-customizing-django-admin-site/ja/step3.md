# 管理変更リストをカスタマイズする

これで `Question` の管理ページが見栄えよくなりましたので、システム内のすべての質問を表示する「変更リスト」ページにいくつかの微調整を加えましょう。

この時点での見た目は以下の通りです。

![Polls 変更リストページ](../assets/admin04t.png)

デフォルトでは、Django は各オブジェクトの `str()` を表示します。しかし、個々のフィールドを表示できる方が時には便利です。そのためには、`~django.contrib.admin.ModelAdmin.list_display` 管理オプションを使用します。これは、オブジェクトの変更リストページに列として表示するフィールド名のタプルです。

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date"]
```

念のため、「データベースの設定」の `was_published_recently()` メソッドも含めましょう。

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

これで質問の変更リストページは以下のようになります。

![Question 変更リストビュー](../assets/20230908-16-14-08-GNY2lggF.png)

列ヘッダーをクリックすると、それらの値でソートできます。ただし、`was_published_recently` ヘッダーの場合は例外です。なぜなら、任意のメソッドの出力でソートすることはサポートされていないからです。また、`was_published_recently` の列ヘッダーは、デフォルトではメソッド名（アンダースコアがスペースに置き換えられています）であり、各行には出力の文字列表現が含まれていることにも注意してください。

それを改善するには、そのメソッド（`polls/models.py` 内）に `~django.contrib.admin.display` デコレータを使用します。以下のようになります。

```python
from django.contrib import admin


class Question(models.Model):
    #...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

デコレータを介して設定可能なプロパティに関する詳細は、`~django.contrib.admin.ModelAdmin.list_display` を参照してください。

もう一度 `polls/admin.py` ファイルを編集し、`Question` の変更リストページに改善を加えましょう。`~django.contrib.admin.ModelAdmin.list_filter` を使用したフィルタリングです。`QuestionAdmin` に以下の行を追加します。

```python
list_filter = ["pub_date"]
```

これにより、「Filter」サイドバーが追加され、`pub_date` フィールドで変更リストをフィルタリングできるようになります。

![管理リストフィルタサイドバー](../assets/20230908-16-16-39-otfMNyYo.png)

表示されるフィルタの種類は、フィルタリング対象のフィールドの種類に依存します。`pub_date` は `~django.db.models.DateTimeField` なので、Django は適切なフィルタオプションを与えることが知っています。「Any date」、「Today」、「Past 7 days」、「This month」、「This year」です。

これはうまくいっています。検索機能を追加しましょう。

```python
search_fields = ["question_text"]
```

これにより、変更リストの上部に検索ボックスが追加されます。誰かが検索用の用語を入力すると、Django は `question_text` フィールドを検索します。好きなだけ多くのフィールドを使用できます。ただし、内部的に `LIKE` クエリを使用するため、検索フィールドの数を合理的な数に制限することで、データベースが検索を行うのが容易になります。

この時点で、変更リストには無料でページネーションが備え付けられていることにも注目してください。デフォルトは 1 ページに 100 件の項目を表示することです。`変更リストのページネーション
<django.contrib.admin.ModelAdmin.list_per_page>`、`検索ボックス
<django.contrib.admin.ModelAdmin.search_fields>`、`フィルタ
<django.contrib.admin.ModelAdmin.list_filter>`、`日付階層
<django.contrib.admin.ModelAdmin.date_hierarchy>`、および `列ヘッダーの並び替え <django.contrib.admin.ModelAdmin.list_display>` はすべて、思った通りに機能します。
