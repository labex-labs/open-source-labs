# 関連オブジェクトの追加

さて、私たちは `Question` の管理ページを持っていますが、`Question` には複数の `Choice` があり、管理ページには選択肢が表示されません。

まだです。

この問題を解決する方法は2つあります。最初の方法は、`Question` の場合と同じように、管理サイトに `Choice` を登録することです。

```python
from django.contrib import admin

from.models import Choice, Question

#...
admin.site.register(Choice)
```

今、「Choices」はDjango管理サイトで利用可能なオプションになりました。「Add choice」フォームは以下のようになっています。

![Add Choiceフォームのインターフェイス](../assets/20230908-16-09-57-eCXIdjZu.png)

そのフォームで、「Question」フィールドはデータベース内のすべての質問を含むセレクトボックスです。Djangoは、`~django.db.models.ForeignKey` が管理サイトで `<select>` ボックスとして表されるべきであることを知っています。私たちの場合、この時点では1つの質問のみが存在します。

また、「Question」の横にある「Add another question」リンクにも注目してください。他のオブジェクトと `ForeignKey` 関係を持つすべてのオブジェクトには、これが自動的に付きます。「Add another question」をクリックすると、「Add question」フォームが表示されるポップアップウィンドウが表示されます。そのウィンドウで質問を追加して「Save」をクリックすると、Djangoは質問をデータベースに保存し、表示している「Add choice」フォームで選択された選択肢として動的に追加します。

しかし、本当に言えば、これはシステムに `Choice` オブジェクトを追加する非効率的な方法です。`Question` オブジェクトを作成する際に、一括で複数の `Choice` を追加できる方が良いでしょう。それを実現しましょう。

`Choice` モデルの `register()` 呼び出しを削除します。そして、`Question` の登録コードを以下のように編集します。

```python
from django.contrib import admin

from.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```

これはDjangoに対して、「`Choice` オブジェクトは `Question` の管理ページで編集されます。デフォルトでは、3つの選択肢用のフィールドを用意します。」と伝えています。

「Add question」ページを読み込んで、その見た目を確認しましょう。

![選択肢付きのQuestion管理](../assets/20230908-16-11-09-tVqaXrGB.png)

動作原理はこうです。関連する `Choice` 用のスロットが3つあります（`extra` によって指定されています）。既に作成済みのオブジェクトの「Change」ページに戻るたびに、追加で3つのスロットが表示されます。

現在の3つのスロットの最後には、「Add another Choice」リンクがあります。これをクリックすると、新しいスロットが追加されます。追加したスロットを削除したい場合は、追加したスロットの右上のXをクリックすることができます。この画像は追加されたスロットを示しています。

![動的に追加された追加スロット](../assets/admin14t.png)

ただし、1つ小さな問題があります。関連する `Choice` オブジェクトを入力するためのすべてのフィールドを表示するには、画面領域が多く必要になります。そのため、Djangoはインライン関連オブジェクトを表示するテーブル形式を提供しています。それを使用するには、`ChoiceInline` の宣言を以下のように変更します。

```python
class ChoiceInline(admin.TabularInline):
  ...
```

この `TabularInline`（`StackedInline` の代わり）を使用すると、関連オブジェクトがよりコンパクトなテーブル形式で表示されます。

![テーブル形式のインライン選択肢表示](../assets/20230908-16-12-24-1nqRkbAI.png)

「Delete?」の追加の列があることに注意してください。これにより、「Add another Choice」ボタンを使用して追加された行や既に保存された行を削除することができます。
