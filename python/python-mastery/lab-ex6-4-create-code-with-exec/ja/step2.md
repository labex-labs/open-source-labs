# 動的な `__init__()` メソッドの作成

ここでは、`exec()` 関数について学んだことを実際のプログラミングシナリオに適用します。Python では、`exec()` 関数を使うと文字列に格納された Python コードを実行することができます。このステップでは、`Structure` クラスを修正して、`__init__()` メソッドを動的に作成します。`__init__()` メソッドは Python クラスの特殊なメソッドで、クラスのオブジェクトがインスタンス化されるときに呼び出されます。このメソッドの作成は、クラスのフィールド名のリストを含む `_fields` クラス変数に基づいて行います。

まず、既存の `structure.py` ファイルを見てみましょう。このファイルには、`Structure` クラスの現在の実装と、それを継承した `Stock` クラスが含まれています。ファイルの内容を表示するには、以下のコマンドを使用して WebIDE で開きます。

```bash
cat /home/labex/project/structure.py
```

出力を見ると、現在の実装ではオブジェクトの初期化を手動で行っていることがわかります。つまり、オブジェクトの属性を初期化するコードは明示的に書かれており、動的に生成されていません。

次に、`Structure` クラスを修正します。`__init__()` メソッドを動的に生成する `create_init()` クラスメソッドを追加します。これらの変更を行うには、WebIDE エディタで `structure.py` ファイルを開き、以下の手順に従います。

1. `Structure` クラスから既存の `_init()` と `set_fields()` メソッドを削除します。これらのメソッドは手動での初期化アプローチの一部であり、動的なアプローチを使用するため、もう必要ありません。

2. `Structure` クラスに `create_init()` クラスメソッドを追加します。以下はこのメソッドのコードです。

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

このメソッドでは、まずフィールド名をカンマで区切った文字列 `argstr` を作成します。この文字列は `__init__()` メソッドの引数リストとして使用されます。次に、`__init__()` メソッドのコードを文字列として作成します。フィールド名をループし、各引数を対応するオブジェクト属性に割り当てる行をコードに追加します。その後、`exec()` 関数を使ってコードを実行し、生成された関数を `locs` 辞書に格納します。最後に、`setattr()` 関数を使って生成された関数をクラスの `__init__()` メソッドとして設定します。

3. `Stock` クラスを修正して、この新しいアプローチを使用するようにします。

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

ここでは、`Stock` クラスの `_fields` を定義し、`create_init()` メソッドを呼び出して `Stock` クラスの `__init__()` メソッドを生成します。

完成した `structure.py` ファイルは次のようになります。

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

では、実装が正しく動作することを確認するためにテストを行いましょう。ユニットテストファイルを実行して、すべてのテストがパスするかどうかを確認します。以下のコマンドを使用します。

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

実装が正しければ、すべてのテストがパスするはずです。これは、動的に生成された `__init__()` メソッドが期待通りに動作していることを意味します。

また、Python シェルで手動でクラスをテストすることもできます。以下のようにします。

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

Python シェルでは、まず `structure.py` ファイルから `Stock` クラスをインポートします。次に、`Stock` クラスのインスタンスを作成して表示します。オブジェクトの `shares` 属性を変更することもできます。ただし、`_fields` リストに存在しない属性を設定しようとすると、`AttributeError` が発生するはずです。

おめでとうございます！`exec()` 関数を使って、クラス属性に基づいて `__init__()` メソッドを動的に作成することに成功しました。このアプローチは、特に属性の数が可変のクラスを扱う場合に、コードをより柔軟で保守しやすくすることができます。
