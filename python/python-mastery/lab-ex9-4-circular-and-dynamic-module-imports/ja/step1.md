# インポートの問題を理解する

まず、モジュールのインポートとは何かを理解しましょう。Pythonでは、別のファイル（モジュール）の関数、クラス、または変数を使用したい場合、`import`文を使用します。ただし、インポートの構造方法によっては、様々な問題が発生することがあります。

では、問題のあるモジュール構造の例を見てみましょう。`tableformat/formatter.py`のコードでは、インポート文がファイル全体に散らばっています。これは最初は大きな問題に見えないかもしれませんが、保守性と依存関係の問題を引き起こします。

まず、WebIDEのファイルエクスプローラを開き、`structly`ディレクトリに移動します。プロジェクトの現在の構造を理解するために、いくつかのコマンドを実行します。`cd`コマンドは現在の作業ディレクトリを変更するために使用され、`ls -la`コマンドは現在のディレクトリ内のすべてのファイルとディレクトリ（隠しファイルも含む）を一覧表示します。

```bash
cd ~/project/structly
ls -la
```

これにより、プロジェクトディレクトリ内のファイルが表示されます。次に、`cat`コマンドを使用して問題のあるファイルの1つを見てみましょう。`cat`コマンドはファイルの内容を表示します。

```bash
cat tableformat/formatter.py
```

以下のようなコードが表示されるはずです。

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

ファイルの途中にインポート文が配置されていることに注意してください。これはいくつかの理由で問題があります。

1. コードの読みやすさと保守性が低下します。ファイルを見るとき、外部モジュールの依存関係をすぐに理解できるように、すべてのインポート文が先頭にあることを期待します。
2. 循環インポート（Circular imports）の問題を引き起こす可能性があります。循環インポートは、2つ以上のモジュールが相互に依存する場合に発生し、エラーを引き起こし、コードが予期せぬ動作をする原因になります。
3. すべてのインポート文をファイルの先頭に配置するというPythonの慣習に違反しています。慣習に従うことで、コードの読みやすさが向上し、他の開発者が理解しやすくなります。

次のステップでは、これらの問題を詳しく調べ、解決方法を学びます。
