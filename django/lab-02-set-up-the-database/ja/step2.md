# モデルの作成

次に、モデルを定義します。基本的には、追加のメタデータ付きのデータベースレイアウトです。

モデルは、データに関する唯一の決定的な情報源です。それは、保存しているデータの必須フィールドと動作を含んでいます。Djangoは「DRY原則 <dry>」に従っています。目的は、データモデルを1か所で定義し、そこから自動的に派生することです。

これにはマイグレーションも含まれます。たとえば、Ruby On Railsとは異なり、マイグレーションは完全にモデルファイルから派生し、本質的には、Djangoがデータベーススキーマを更新して現在のモデルに合わせるためにロールバックできる履歴です。

投票アプリでは、2つのモデルを作成します。`Question` と `Choice`。`Question` には質問と公開日があります。`Choice` には2つのフィールドがあります。選択肢のテキストと投票数です。各 `Choice` は1つの `Question` に関連付けられています。

これらの概念はPythonクラスで表されます。`polls/models.py` ファイルを編集して、以下のようにします。

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

ここでは、各モデルは `django.db.models.Model` をサブクラス化するクラスで表されています。各モデルには多くのクラス変数があり、それぞれがモデル内のデータベースフィールドを表しています。

各フィールドは `~django.db.models.Field` クラスのインスタンスで表されます。たとえば、文字列フィールドの場合は `~django.db.models.CharField`、日付時刻の場合は `~django.db.models.DateTimeField` です。これにより、Djangoに各フィールドが保持するデータの型がわかります。

各 `~django.db.models.Field` インスタンスの名前（たとえば `question_text` または `pub_date`）は、機械が読み取りやすい形式のフィールド名です。Pythonコードでこの値を使用し、データベースでは列名として使用されます。

`~django.db.models.Field` には、オプションの最初の位置引数を使用して、人間が読みやすい名前を指定できます。これは、Djangoのいくつかの内省的な部分で使用され、ドキュメントとしても役立ちます。このフィールドが指定されない場合、Djangoは機械が読み取りやすい名前を使用します。この例では、`Question.pub_date` にのみ人間が読みやすい名前を定義しています。このモデルの他のすべてのフィールドについては、フィールドの機械が読み取りやすい名前が人間が読みやすい名前として十分です。

一部の `~django.db.models.Field` クラスには必須引数があります。たとえば、`~django.db.models.CharField` には `~django.db.models.CharField.max_length` を指定する必要があります。これは、データベーススキーマだけでなく、検証にも使用されます。これは後で説明します。

`~django.db.models.Field` にはさまざまなオプション引数もあります。この場合、`votes` の `~django.db.models.Field.default` 値を0に設定しています。

最後に、`~django.db.models.ForeignKey` を使用して関係が定義されていることに注意してください。これにより、Djangoに各 `Choice` が1つの `Question` に関連付けられていることがわかります。Djangoは、多対1、多対多、1対1のすべての一般的なデータベース関係をサポートしています。
