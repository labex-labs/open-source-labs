# パッケージからの全シンボルエクスポート

Python では、コードを効果的に管理するためにパッケージの組織化が重要です。今回は、パッケージの組織化をさらに進めます。パッケージレベルでどのシンボルをエクスポートするかを定義します。シンボルをエクスポートするとは、特定の関数、クラス、または変数をコードの他の部分や、あなたのパッケージを使用する可能性のある他の開発者に利用可能にすることを意味します。

## パッケージに `__all__` を追加する

Python パッケージを扱う際に、`from structly import *` 文を使用したときにどのシンボルにアクセスできるかを制御したいことがあります。このような場合に `__all__` リストが便利です。パッケージの `__init__.py` ファイルに `__all__` リストを追加することで、`from structly import *` 文を使用したときにどのシンボルが利用可能かを正確に制御できます。

まず、`__init__.py` ファイルを作成または更新しましょう。ファイルが存在しない場合は `touch` コマンドを使用して作成します。

```bash
touch ~/project/structly/__init__.py
```

次に、`__init__.py` ファイルを開き、`__all__` リストを追加します。このリストには、エクスポートしたいすべてのシンボルを含める必要があります。シンボルは、それらが由来する場所（例えば `structure`、`reader`、`tableformat` モジュール）に基づいてグループ化されます。

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

コードを追加したら、ファイルを保存し、エディタを終了します。

## `import *` の理解

`from module import *` パターンは、ほとんどの Python コードでは一般的に推奨されていません。これにはいくつかの理由があります。

1. 予期しないシンボルで名前空間を汚染する可能性があります。これは、現在の名前空間に予期しない変数や関数が含まれることを意味し、名前の衝突につながる可能性があります。
2. 特定のシンボルがどこから来たかが不明確になります。`import *` を使用すると、シンボルがどのモジュールから来ているかを判断するのが難しく、コードの理解と保守が困難になります。
3. シャドウイング（shadowing）の問題を引き起こす可能性があります。シャドウイングは、ローカル変数または関数が他のモジュールの変数または関数と同じ名前を持っている場合に発生し、予期しない動作を引き起こす可能性があります。

ただし、`import *` を使用するのが適切な特定のケースもあります。

- まとまった単位として使用することを想定したパッケージの場合。パッケージが単一のユニットとして使用されることを意図している場合、`import *` を使用すると、必要なすべてのシンボルにアクセスしやすくなります。
- パッケージが `__all__` を介して明確なインターフェースを定義している場合。`__all__` リストを使用することで、エクスポートされるシンボルを制御できるため、`import *` を安全に使用できます。
- Python REPL（Read-Eval-Print Loop）のような対話的な使用の場合。対話的な環境では、一度にすべてのシンボルをインポートするのが便利なことがあります。

## `import *` でのテスト

一度にすべてのシンボルをインポートできることを確認するために、別のテストファイルを作成しましょう。`touch` コマンドを使用してファイルを作成します。

```bash
touch ~/project/test_import_all.py
```

次に、`test_import_all.py` ファイルを開き、以下の内容を追加します。このコードは、`structly` パッケージからすべてのシンボルをインポートし、いくつかの重要なシンボルが利用可能かどうかをテストします。

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

ファイルを保存し、エディタを終了します。では、テストを実行しましょう。まず、`cd` コマンドを使用してプロジェクトディレクトリに移動し、その後 Python スクリプトを実行します。

```bash
cd ~/project
python test_import_all.py
```

すべてが正しく設定されている場合、すべてのシンボルが正常にインポートされたことを確認できるはずです。
