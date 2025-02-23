# APIを使ってみる

次に、対話型のPythonシェルに入り、Djangoが提供する無料のAPIを試してみましょう。Pythonシェルを起動するには、次のコマンドを使用します。

```bash
python manage.py shell
```

単に「python」と入力する代わりにこれを使用しているのは、`manage.py` が `DJANGO_SETTINGS_MODULE` 環境変数を設定するためで、これによりDjangoに `mysite/settings.py` ファイルのPythonインポートパスがわかります。

シェルに入ったら、`データベースAPI </topics/db/queries>` を調べてみましょう。

```python
>>> from polls.models import Choice, Question  # 先ほど書いたモデルクラスをインポートする。

# システムにはまだ質問がありません。
>>> Question.objects.all()
<QuerySet []>

# 新しい質問を作成する。
# デフォルトの設定ファイルではタイムゾーンのサポートが有効になっているため、
# Djangoはpub_dateにtzinfo付きのdatetimeを期待します。timezone.now()を使用して
# datetime.datetime.now()の代わりに使用すると、正しい処理が行われます。
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# オブジェクトをデータベースに保存する。save()を明示的に呼び出す必要があります。
>>> q.save()

# 今やIDがあります。
>>> q.id
1

# Python属性を介してモデルフィールドの値にアクセスする。
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# 属性を変更してからsave()を呼び出すことで値を変更する。
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all()はデータベース内のすべての質問を表示する。
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

ちょっと待ってください。`<Question: Question object (1)>` はこのオブジェクトの分かりやすい表現ではありません。`Question` モデル（`polls/models.py` ファイル内）を編集して、`Question` と `Choice` の両方に `~django.db.models.Model.__str__` メソッドを追加することで、これを修正しましょう。

```python
from django.db import models


class Question(models.Model):
    #...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
```

モデルに `~django.db.models.Model.__str__` メソッドを追加することは重要です。対話型プロンプトを扱う際に自分自身の利便性のためだけでなく、Djangoの自動生成の管理サイト全体でオブジェクトの表現が使用されるためです。

このモデルにカスタムメソッドも追加しましょう。

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

`import datetime` と `from django.utils import timezone` の追加に注目してください。それぞれ、Pythonの標準の `datetime` モジュールと、`django.utils.timezone` 内のDjangoのタイムゾーン関連のユーティリティを参照するために使用されます。Pythonでのタイムゾーンの処理に慣れていない場合は、`タイムゾーンサポートドキュメント </topics/i18n/timezones>` で詳しく学ぶことができます。

これらの変更を保存し、再度 **`python manage.py shell` を実行** して新しいPython対話型シェルを起動します。

```python
>>> from polls.models import Choice, Question

# 私たちの__str__()の追加が機能したことを確認する。
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Djangoはキーワード引数によって完全に駆動される豊富なデータベース検索APIを提供しています。
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# 今年公開された質問を取得する。
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# 存在しないIDを要求すると、例外が発生します。
>>> Question.objects.get(id=2)
Traceback (most recent call last):
 ...
DoesNotExist: Question matching query does not exist.

# 主キーによる検索は最も一般的なケースなので、Djangoは主キーの完全一致検索用のショートカットを提供しています。
# 以下はQuestion.objects.get(id=1)と同じです。
>>> Question.objects.get(pk=1)
<Question: What's up?>

# 私たちのカスタムメソッドが機能したことを確認する。
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# この質問にいくつかの選択肢を与える。create呼び出しは新しい
# Choiceオブジェクトを構築し、INSERT文を行い、利用可能な選択肢のセットに選択肢を追加し、新しいChoiceオブジェクトを返します。Djangoは
# 外部キー関係の「他方」（たとえば質問の選択肢）を保持するセットを作成し、APIを介してアクセスできます。
>>> q = Question.objects.get(pk=1)

# 関連オブジェクトセットからの選択肢を表示する -- 今のところはありません。
>>> q.choice_set.all()
<QuerySet []>

# 3つの選択肢を作成する。
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choiceオブジェクトは関連するQuestionオブジェクトにAPIアクセスを持っています。
>>> c.question
<Question: What's up?>

# 逆も同様です。QuestionオブジェクトはChoiceオブジェクトにアクセスします。
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# APIは必要な限り関係を自動的に辿ります。
# 関係を区切るには2つのアンダースコアを使用します。
# これは必要なだけ深く機能します。制限はありません。
# 今年の公開日付を持つ任意の質問のすべての選択肢を見つける
# （上で作成した'current_year'変数を再利用）。
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# 選択肢の1つを削除しましょう。delete()を使用します。
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

モデル関係の詳細については、`関連オブジェクトのアクセス
</ref/models/relations>` を参照してください。APIを介してフィールド検索を行う際の2つのアンダースコアの使用方法については、`フィールド検索 <field-lookups-intro>` を参照してください。データベースAPIの詳細については、`データベースAPIリファレンス
</topics/db/queries>` を参照してください。
