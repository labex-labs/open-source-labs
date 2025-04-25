# チャレンジ：呼び出し可能オブジェクトをメソッドとして使用する

Python では、呼び出し可能オブジェクトをクラス内のメソッドとして使用する場合、独自の課題に直面することがあります。呼び出し可能オブジェクトとは、関数のように「呼び出す」ことができるもので、関数自体や `__call__` メソッドを持つオブジェクトなどが該当します。クラスメソッドとして使用すると、Python がインスタンス (`self`) を最初の引数として渡す仕組みのため、必ずしも期待通りに動作しないことがあります。

この問題を `Stock` クラスを作成することで探ってみましょう。このクラスは、名前、株式数、価格などの属性を持つ株式を表します。また、取り扱うデータが正しいことを確認するためにバリデータを使用します。

まず、`Stock` クラスを記述するために `stock.py` ファイルを開きます。以下のコマンドを使用してエディタでファイルを開くことができます。

```bash
code /home/labex/project/stock.py
```

次に、`stock.py` ファイルに以下のコードを追加します。このコードは、株式の属性を初期化する `__init__` メソッド、総コストを計算する `cost` プロパティ、株式数を減らす `sell` メソッドを持つ `Stock` クラスを定義します。また、`sell` メソッドの入力を検証するために `ValidatedFunction` を使用しようとします。

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

`Stock` クラスを定義した後、期待通りに動作するかどうかをテストする必要があります。`test_stock.py` という名前のテストファイルを作成し、以下のコマンドを使用して開きます。

```bash
code /home/labex/project/test_stock.py
```

`test_stock.py` ファイルに以下のコードを追加します。このコードは、`Stock` クラスのインスタンスを作成し、初期の株式数とコストを表示し、いくつかの株式を売却しようとし、その後更新された株式数とコストを表示します。

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

次に、以下のコマンドを使用してテストファイルを実行します。

```bash
python3 /home/labex/project/test_stock.py
```

おそらく、以下のようなエラーが発生するでしょう。

```
Error: missing a required argument: 'nshares'
```

このエラーが発生するのは、Python が `s.sell(10)` のようなメソッドを呼び出すとき、実際には `Stock.sell(s, 10)` を呼び出すためです。`self` パラメータはクラスのインスタンスを表し、最初の引数として自動的に渡されます。しかし、`ValidatedFunction` はこの `self` パラメータを正しく処理できません。なぜなら、メソッドとして使用されていることを認識していないからです。

**問題の理解**

クラス内でメソッドを定義し、それを `ValidatedFunction` で置き換えると、実質的に元のメソッドをラップすることになります。問題は、ラップされたメソッドが `self` パラメータを正しく自動的に処理しないことです。インスタンスが最初の引数として渡されることを考慮していない形で引数を期待しています。

**問題の解決**

この問題を解決するには、メソッドの処理方法を変更する必要があります。メソッド呼び出しを適切に処理できる `ValidatedMethod` という新しいクラスを作成します。`validate.py` ファイルの末尾に以下のコードを追加します。

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

次に、`Stock` クラスを変更して `ValidatedFunction` の代わりに `ValidatedMethod` を使用するようにします。再度 `stock.py` ファイルを開きます。

```bash
code /home/labex/project/stock.py
```

`Stock` クラスを以下のように更新します。

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

`ValidatedMethod` クラスはディスクリプタです。ディスクリプタは、属性のアクセス方法を変更できる Python の特殊なオブジェクトです。`__get__` メソッドは、属性がメソッドとしてアクセスされたときに呼び出されます。このメソッドは、インスタンスを最初の引数として正しく渡す呼び出し可能オブジェクトを返します。

以下のコマンドを使用して再度テストファイルを実行します。

```bash
python3 /home/labex/project/test_stock.py
```

今度は、以下のような出力が表示されるはずです。

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

このチャレンジは、呼び出し可能オブジェクトの重要な側面を示しています。クラス内のメソッドとして使用する場合、特別な処理が必要です。`__get__` メソッドを使用してディスクリプタプロトコルを実装することで、スタンドアロン関数としてもメソッドとしても正しく動作する呼び出し可能オブジェクトを作成することができます。
