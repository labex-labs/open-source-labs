# 動的インポート（Dynamic Imports）の使用

プログラミングにおいて、インポート（import）は他のモジュールからコードを取り込み、その機能を利用するために使用されます。しかし、時にはファイルの途中にインポート文があると、コードが少し混乱しやすく、理解しにくくなることがあります。このセクションでは、この問題を解決するために動的インポート（Dynamic imports）を使用する方法を学びます。動的インポートは、実行時にモジュールをロードできる強力な機能です。つまり、実際に必要なときにのみモジュールをロードすることができます。

まず、`TableFormatter`クラスの後に配置されているインポート文を削除する必要があります。これらのインポートは静的インポート（Static imports）であり、プログラムが起動するときにロードされます。これを行うには、WebIDE で`tableformat/formatter.py`ファイルを開きます。ファイルを開いたら、次の行を見つけて削除します。

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

ここで、ターミナルで次のコマンドを実行してプログラムを実行しようとすると：

```bash
python3 stock.py
```

プログラムは失敗します。その理由は、フォーマッターが`_formats`辞書に登録されていないからです。不明なフォーマットに関するエラーメッセージが表示されます。これは、プログラムが適切に動作するために必要なフォーマッタークラスを見つけることができないからです。

この問題を解決するために、`create_formatter`関数を変更します。目的は、必要なモジュールを必要なときに動的にインポートすることです。関数を以下のように更新します。

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

この関数で最も重要な行は：

```python
__import__(f'{__package__}.formats.{name}')
```

この行は、フォーマット名に基づいてモジュールを動的にインポートします。モジュールがインポートされると、その`TableFormatter`のサブクラスは自動的に自身を登録します。これは、先ほど追加した`__init_subclass__`メソッドのおかげです。このメソッドは、サブクラスが作成されたときに呼び出される Python の特殊メソッドであり、このケースではフォーマッタークラスを登録するために使用されます。

これらの変更を加えた後、ファイルを保存します。次に、次のコマンドを使用してプログラムを再度実行します。

```bash
python3 stock.py
```

静的インポートを削除したにもかかわらず、プログラムは正常に動作するはずです。動的インポートが期待通りに動作していることを確認するために、`_formats`辞書をクリアしてから`create_formatter`関数を呼び出します。ターミナルで次のコマンドを実行します。

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

次のような出力が表示されるはずです。

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

この出力は、動的インポートが必要なときにモジュールをロードし、フォーマッタークラスを登録していることを確認しています。

動的インポートとクラス登録を使用することで、よりクリーンで保守しやすいコード構造を作成しました。以下はその利点です。

1. すべてのインポート文がファイルの先頭にあり、Python の慣習に沿っています。これにより、コードが読みやすく理解しやすくなります。
2. 循環インポート（Circular imports）を排除しました。循環インポートは、無限ループやデバッグが困難なエラーなど、プログラムに問題を引き起こす可能性があります。
3. コードがより柔軟になりました。現在では、`create_formatter`関数を変更することなく新しいフォーマッターを追加することができます。これは、新しい機能が時間とともに追加される実際のシナリオで非常に有用です。

動的インポートとクラス登録を使用するこのパターンは、プラグインシステムやフレームワークで一般的に使用されています。これらのシステムでは、コンポーネントをユーザーのニーズやプログラムの要件に基づいて動的にロードする必要があります。
