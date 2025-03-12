# ディスクリプタ実装の改善

このステップでは、ディスクリプタの実装を強化します。場合によっては、名前を冗長に指定していることに気づいたかもしれません。これはコードを少し混乱させ、保守が難しくなる可能性があります。この問題を解決するために、Python 3.6 で導入された便利な機能である `__set_name__` メソッドを使用します。

`__set_name__` メソッドは、クラスが定義されると自動的に呼び出されます。その主な役割は、ディスクリプタの名前を自動的に設定することで、毎回手動で設定する必要がなくなります。これにより、コードがクリーンで効率的になります。

では、`validate.py` ファイルを更新して `__set_name__` メソッドを追加しましょう。更新後のコードは次のようになります。

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
            self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

上記のコードでは、`Validator` クラスの `__set_name__` メソッドが `name` 属性が `None` かどうかをチェックします。もし `None` であれば、`name` をクラス定義で使用される実際の属性名に設定します。このようにして、ディスクリプタクラスのインスタンスを作成するときに名前を明示的に指定する必要がなくなります。

`validate.py` ファイルを更新したので、`Stock` クラスの改良版を作成できます。この新しいバージョンでは、名前を冗長に指定する必要がありません。改良版の `Stock` クラスのコードは次の通りです。

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

この `Stock` クラスでは、`String`、`PositiveInteger`、`PositiveFloat` ディスクリプタクラスのインスタンスを名前を指定せずに作成しています。`Validator` クラスの `__set_name__` メソッドが名前を自動的に設定します。

改良版の `Stock` クラスをテストしましょう。まず、ターミナルを開き、プロジェクトディレクトリに移動します。次に、対話モードで `improved_stock.py` ファイルを実行します。以下はそのためのコマンドです。

```bash
cd ~/project
python3 -i improved_stock.py
```

対話型 Python セッションに入ったら、次のコマンドを試して `Stock` クラスの機能をテストできます。

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

これらのコマンドは、`Stock` クラスのインスタンスを作成し、その属性を印刷し、属性の値を変更し、そして無効な値を設定して適切なエラーが発生するかどうかを確認します。

`__set_name__` メソッドは、クラスが定義されるときにディスクリプタの名前を自動的に設定します。これにより、属性名を 2 回指定する必要がなくなり、コードがクリーンで冗長性が減ります。

この改善は、Python のディスクリプタプロトコルがどのように進化し、クリーンで保守可能なコードを書きやすくしているかを示しています。
