# コードの整理のためのモジュール分割

Python プロジェクトが拡大するにつれて、単一のモジュールファイルが非常に大きくなり、関連するが異なる複数のコンポーネントを含むようになることがあります。このような場合、モジュールをサブモジュールを持つパッケージに分割するのが良いプラクティスです。このアプローチにより、コードがより整理され、保守が容易になり、拡張性も向上します。

## 現在の構造の理解

`tableformat.py` モジュールは、大きなモジュールの良い例です。このモジュールにはいくつかのフォーマッタクラスが含まれており、それぞれが異なる方法でデータをフォーマットする役割を持っています。

- `TableFormatter` (基底クラス): これは他のすべてのフォーマッタクラスの基底クラスです。他のクラスが継承して実装する基本的な構造とメソッドを定義しています。
- `TextTableFormatter`: このクラスはデータをプレーンテキストでフォーマットします。
- `CSVTableFormatter`: このクラスはデータを CSV (Comma-Separated Values) 形式でフォーマットします。
- `HTMLTableFormatter`: このクラスはデータを HTML (Hypertext Markup Language) 形式でフォーマットします。

このモジュールを、各フォーマッタタイプに対して別々のファイルを持つパッケージ構造に再編成します。これにより、コードがよりモジュール化され、管理が容易になります。

## ステップ 1: キャッシュファイルのクリーンアップ

コードを再編成する前に、Python のキャッシュファイルをクリーンアップするのが良い考えです。これらのファイルは Python によって作成され、コードの実行を高速化するためのものですが、コードを変更する際に問題を引き起こすことがあります。

```bash
cd ~/project/structly
rm -rf __pycache__
```

上記のコマンドで、`cd ~/project/structly` は現在のディレクトリをプロジェクトの `structly` ディレクトリに変更します。`rm -rf __pycache__` は `__pycache__` ディレクトリとそのすべての内容を削除します。`-r` オプションは再帰的 (recursive) を意味し、`__pycache__` ディレクトリ内のすべてのファイルとサブディレクトリを削除します。`-f` オプションは強制 (force) を意味し、確認を求めることなくファイルを削除します。

## ステップ 2: 新しいパッケージ構造の作成

では、パッケージの新しいディレクトリ構造を作成しましょう。`tableformat` という名前のディレクトリと、その中に `formats` という名前のサブディレクトリを作成します。

```bash
mkdir -p tableformat/formats
```

`mkdir` コマンドはディレクトリを作成するために使用されます。`-p` オプションは親ディレクトリ (parents) を意味し、必要なすべての親ディレクトリが存在しない場合に作成します。したがって、`tableformat` ディレクトリが存在しない場合は最初に作成され、その後 `formats` ディレクトリがその中に作成されます。

## ステップ 3: 元のファイルの移動と名前変更

次に、元の `tableformat.py` ファイルを新しい構造に移動し、`formatter.py` に名前を変更します。

```bash
mv tableformat.py tableformat/formatter.py
```

`mv` コマンドはファイルを移動または名前変更するために使用されます。この場合、`tableformat.py` ファイルを `tableformat` ディレクトリに移動し、`formatter.py` に名前を変更しています。

## ステップ 4: コードを別々のファイルに分割する

ここで、各フォーマッタ用のファイルを作成し、関連するコードをそれらに移動する必要があります。

### 1. 基底フォーマッタファイルの作成

```bash
touch tableformat/formatter.py
```

`touch` コマンドは空のファイルを作成するために使用されます。この場合、`tableformat` ディレクトリに `formatter.py` という名前のファイルを作成しています。

このファイルには、`TableFormatter` 基底クラスと `print_table` や `create_formatter` のような一般的なユーティリティ関数を保持します。ファイルは次のようになるはずです。

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

`__all__` 変数は、`from module import *` を使用したときにインポートされるシンボルを指定するために使用されます。この場合、`TableFormatter`、`print_table`、`create_formatter` シンボルのみがインポートされるように指定しています。

`TableFormatter` クラスは他のすべてのフォーマッタクラスの基底クラスです。`headings` と `row` の 2 つのメソッドを定義しており、サブクラスによって実装されることを意図しています。

`print_table` 関数は、オブジェクトのリスト、列名のリスト、およびフォーマッタオブジェクトを受け取り、データを整形された表形式で出力するユーティリティ関数です。

`create_formatter` 関数は、フォーマット名を引数として受け取り、適切なフォーマッタオブジェクトを返すファクトリ関数です。

これらの変更を加えた後、ファイルを保存して終了します。

### 2. テキストフォーマッタの作成

```bash
touch tableformat/formats/text.py
```

このファイルには `TextTableFormatter` クラスのみを追加します。

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

`__all__` 変数は、`from module import *` を使用したときにインポートされるシンボルを指定しており、この場合 `TextTableFormatter` シンボルのみがインポートされるように指定しています。

`from ..formatter import TableFormatter` 文は、親ディレクトリの `formatter.py` ファイルから `TableFormatter` クラスをインポートします。

`TextTableFormatter` クラスは `TableFormatter` クラスを継承し、`headings` と `row` メソッドを実装してデータをプレーンテキストでフォーマットします。

これらの変更を加えた後、ファイルを保存して終了します。

### 3. CSV フォーマッタの作成

```bash
touch tableformat/formats/csv.py
```

このファイルには `CSVTableFormatter` クラスのみを追加します。

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

前のステップと同様に、`__all__` 変数を指定し、`TableFormatter` クラスをインポートし、`headings` と `row` メソッドを実装してデータを CSV 形式でフォーマットします。

これらの変更を加えた後、ファイルを保存して終了します。

### 4. HTML フォーマッタの作成

```bash
touch tableformat/formats/html.py
```

このファイルには `HTMLTableFormatter` クラスのみを追加します。

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

再び、`__all__` 変数を指定し、`TableFormatter` クラスをインポートし、`headings` と `row` メソッドを実装してデータを HTML 形式でフォーマットします。

これらの変更を加えた後、ファイルを保存して終了します。

## ステップ 5: パッケージ初期化ファイルの作成

Python では、`__init__.py` ファイルはディレクトリを Python パッケージとしてマークするために使用されます。`tableformat` と `formats` の両方のディレクトリに `__init__.py` ファイルを作成する必要があります。

### 1. `tableformat` パッケージ用のファイルを作成する

```bash
touch tableformat/__init__.py
```

ファイルに次の内容を追加します。

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

この文は `formatter.py` ファイルからすべてのシンボルをインポートし、`tableformat` パッケージをインポートしたときにそれらを利用可能にします。

これらの変更を加えた後、ファイルを保存して終了します。

### 2. `formats` パッケージ用のファイルを作成する

```bash
touch tableformat/formats/__init__.py
```

このファイルは空のままにしても、簡単なドキュメント文字列を追加しても構いません。

```python
'''
Format implementations for different output formats.
'''
```

ドキュメント文字列は、`formats` パッケージの機能について簡単な説明を提供します。

これらの変更を加えた後、ファイルを保存して終了します。

## ステップ 6: 新しい構造のテスト

変更が正しく機能することを確認するために、簡単なテストを作成しましょう。

```bash
cd ~/project
touch test_tableformat.py
```

`test_tableformat.py` ファイルに次の内容を追加します。

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

このテストコードは、`structly` パッケージから必要な関数とクラスをインポートし、各タイプのフォーマッタを作成し、いくつかのテストデータを定義し、それぞれのフォーマッタをテストしてデータを対応する形式で出力します。

これらの変更を加えた後、ファイルを保存して終了します。では、テストを実行しましょう。

```bash
python test_tableformat.py
```

同じデータが 3 つの異なる形式（テキスト、CSV、HTML）でフォーマットされた結果が表示されるはずです。期待される出力が表示されれば、コードの再編成が成功したことを意味します。
