# `__all__` を使用したエクスポートシンボルの制御

Python で `from module import *` 文を使用する場合、モジュールからインポートするシンボル（関数、クラス、変数）を制御したいことがあります。このような場合に `__all__` 変数が便利です。`from module import *` 文は、モジュール内のすべてのシンボルを現在の名前空間にインポートする方法です。ただし、場合によってはすべてのシンボルをインポートしたくないことがあります。特に、シンボルが多数ある場合や、一部のシンボルがモジュール内部で使用するものである場合です。`__all__` 変数を使用すると、この文を使用したときに具体的にどのシンボルをインポートするかを指定できます。

## `__all__` とは何か？

`__all__` 変数は文字列のリストです。このリスト内の各文字列は、`from module import *` 文を使用したときにモジュールがエクスポートするシンボル（関数、クラス、または変数）を表します。モジュール内で `__all__` 変数が定義されていない場合、`import *` 文はアンダースコアで始まらないすべてのシンボルをインポートします。アンダースコアで始まるシンボルは、通常、モジュールのプライベートまたは内部用と見なされ、直接インポートすることを意図していません。

## 各サブモジュールの修正

では、`structly` パッケージ内の各サブモジュールに `__all__` 変数を追加しましょう。これにより、`from module import *` 文を使用したときに各サブモジュールからエクスポートされるシンボルを制御できます。

1. まず、`structure.py` を修正しましょう。

```bash
touch ~/project/structly/structure.py
```

このコマンドは、プロジェクトの `structly` ディレクトリに `structure.py` という名前の新しいファイルを作成します。ファイルを作成した後、`__all__` 変数を追加する必要があります。インポート文の直後、ファイルの上部近くに次の行を追加します。

```python
__all__ = ['Structure']
```

この行は、`from structure import *` を使用した場合、`Structure` シンボルのみがインポートされることを Python に伝えます。ファイルを保存し、エディタを終了します。

2. 次に、`reader.py` を修正しましょう。

```bash
touch ~/project/structly/reader.py
```

このコマンドは、`structly` ディレクトリに `reader.py` という名前の新しいファイルを作成します。今度は、ファイルを調べて `read_csv_as_` で始まるすべての関数を見つけます。これらの関数がエクスポートしたい関数です。そして、これらの関数名をすべて含む `__all__` リストを追加します。次のようになります。

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

実際の関数名は、ファイル内にあるものによって異なる場合があります。見つけたすべての `read_csv_as_*` 関数を含めるようにしてください。ファイルを保存し、エディタを終了します。

3. では、`tableformat.py` を修正しましょう。

```bash
touch ~/project/structly/tableformat.py
```

このコマンドは、`structly` ディレクトリに `tableformat.py` という名前の新しいファイルを作成します。ファイルの上部近くに次の行を追加します。

```python
__all__ = ['create_formatter', 'print_table']
```

この行は、`from tableformat import *` を使用した場合、`create_formatter` と `print_table` シンボルのみがインポートされることを指定します。ファイルを保存し、エディタを終了します。

## `__init__.py` での統一的なインポート

各モジュールがエクスポートするものを定義したので、`__init__.py` ファイルを更新してこれらのすべてのシンボルをインポートできます。`__init__.py` ファイルは Python パッケージにおける特別なファイルです。パッケージがインポートされると実行され、パッケージを初期化したり、サブモジュールからシンボルをインポートしたりするために使用できます。

```bash
touch ~/project/structly/__init__.py
```

このコマンドは、`structly` ディレクトリに新しい `__init__.py` ファイルを作成します。ファイルの内容を次のように変更します。

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

これらの行は、`structure`、`reader`、および `tableformat` サブモジュールからすべてのエクスポートされたシンボルをインポートします。モジュール名の前のドット (`.`) は、これらが相対インポートであることを示しており、同じパッケージ内からのインポートであることを意味します。ファイルを保存し、エディタを終了します。

## 変更のテスト

変更が機能することを確認するために、簡単なテストファイルを作成しましょう。このテストファイルは、`__all__` 変数で指定したシンボルをインポートしようとし、インポートが成功した場合は成功メッセージを表示します。

```bash
touch ~/project/test_structly.py
```

このコマンドは、プロジェクトディレクトリに `test_structly.py` という名前の新しいファイルを作成します。ファイルに次の内容を追加します。

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

これらの行は、`structly` パッケージから `Structure` クラス、`read_csv_as_instances` 関数、および `create_formatter` と `print_table` 関数をインポートしようとします。インポートが成功した場合、プログラムは「Successfully imported all required symbols!」というメッセージを表示します。ファイルを保存し、エディタを終了します。では、このテストを実行しましょう。

```bash
cd ~/project
python test_structly.py
```

`cd ~/project` コマンドは、現在の作業ディレクトリをプロジェクトディレクトリに変更します。`python test_structly.py` コマンドは、`test_structly.py` スクリプトを実行します。すべてが正しく動作している場合、画面に「Successfully imported all required symbols!」というメッセージが表示されるはずです。
