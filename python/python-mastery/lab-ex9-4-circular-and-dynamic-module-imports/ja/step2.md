# 循環インポート（Circular Imports）を調べる

循環インポート（Circular import）とは、2つ以上のモジュールが相互に依存する状況です。具体的には、モジュールAがモジュールBをインポートし、モジュールBも直接的または間接的にモジュールAをインポートする場合です。これにより、Pythonのインポートシステムが適切に解決できない依存関係のループが生じます。簡単に言えば、Pythonはどのモジュールを最初にインポートするかを判断するためにループに陥り、これがプログラムでエラーを引き起こす可能性があります。

コードを使って実験し、循環インポートがどのように問題を引き起こすかを見てみましょう。

まず、現在の構造で在庫管理プログラムが動作するかどうかを確認します。このステップでは、基準を設定し、何かを変更する前にプログラムが期待通りに動作することを確認します。

```bash
cd ~/project/structly
python3 stock.py
```

プログラムは正常に実行され、在庫データが整形された表形式で表示されるはずです。もしそうであれば、現在のコード構造は循環インポートの問題なしに正常に動作していることを意味します。

次に、`formatter.py`ファイルを変更します。通常、インポート文をファイルの先頭に移動するのは良い習慣です。これにより、コードが整理され、一目で理解しやすくなります。

```bash
cd ~/project/structly
```

WebIDEで`tableformat/formatter.py`を開きます。以下のインポート文を既存のインポート文の直後、ファイルの先頭に移動します。これらのインポート文は、テキスト、CSV、HTMLなどの異なる表形式のフォーマッターに関するものです。

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

これで、ファイルの先頭は次のようになるはずです。

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

ファイルを保存し、在庫管理プログラムを再度実行してみましょう。

```bash
python3 stock.py
```

`TableFormatter`が定義されていないというエラーメッセージが表示されるはずです。これは循環インポートの問題の明確な兆候です。

この問題は、以下の一連のイベントによって発生します。

1. `formatter.py`が`formats/text.py`から`TextTableFormatter`をインポートしようとします。
2. `formats/text.py`が`formatter.py`から`TableFormatter`をインポートします。
3. Pythonがこれらのインポートを解決しようとすると、どのモジュールを最初に完全にインポートするかを決定できないため、ループに陥ります。

プログラムを再度動作させるために、変更を元に戻しましょう。`tableformat/formatter.py`を編集し、インポート文を元の位置（`TableFormatter`クラス定義の後）に戻します。

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
```

プログラムが動作していることを確認するために、再度実行します。

```bash
python3 stock.py
```

これは、コードの整理の観点からインポート文をファイルの途中に配置するのは最善の方法ではないものの、循環インポートの問題を回避するために行われたことを示しています。次のステップでは、より良い解決策を探ります。
