# 管理フォームをカスタマイズする

`admin.site.register(Question)` で `Question` モデルを登録することで、Django はデフォルムの表現を構築することができました。多くの場合、管理フォームの見た目や動作をカスタマイズしたいと思うでしょう。これは、オブジェクトを登録する際に Django に望むオプションを伝えることで行います。

編集フォームのフィールドの順序を変更することで、これがどのように機能するか見てみましょう。`admin.site.register(Question)` 行を以下のものに置き換えます。

`~/project/mysite/polls/admin.py` ファイルを編集して、以下のようになるようにします。

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
```

このパターンに従います。モデル管理クラスを作成し、それを `admin.site.register()` の 2 番目の引数として渡します。モデルの管理オプションを変更する必要があるときはいつでもこれを行います。

Django 開発サーバーを起動します。

```bash
cd ~/project/mysite
python manage.py runserver
```

デスクトップ環境の Firefox で `http://127.0.0.1:8000/admin/` を開き、「Questions」リンクをクリックします。以下のようなフォームが表示されるはずです。

上記の特定の変更により、「Publication date」が「Question」フィールドの前に表示されるようになります。

![管理フォームのフィールドの並び替え](../assets/20230908-16-06-41-wiBfnHS8.png)

2 つのフィールドだけでは印象的ではありませんが、数十個のフィールドを持つ管理フォームの場合、直感的な順序を選ぶことは重要なユーザビリティの詳細です。

そして、数十個のフィールドを持つフォームについて言えば、フォームをフィールドセットに分割したい場合があります。

```python
from django.contrib import admin

from.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
```

`~django.contrib.admin.ModelAdmin.fieldsets` の各タプルの最初の要素は、フィールドセットのタイトルです。これが現在のフォームの見た目です。

![フィールドセット付きの管理フォーム](../assets/20230908-16-08-19-HOzMJWFG.png)
