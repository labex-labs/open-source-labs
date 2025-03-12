# ディスクリプタを使用したバリデータの実装

このステップでは、ディスクリプタを使用してバリデーションシステムを作成します。まず、ディスクリプタとは何か、なぜそれを使用するのかを理解しましょう。ディスクリプタは、`__get__`、`__set__`、または `__delete__` メソッドを含むディスクリプタプロトコルを実装した Python オブジェクトです。これらを使用すると、オブジェクトの属性のアクセス、設定、または削除方法をカスタマイズできます。今回のケースでは、ディスクリプタを使用してデータの整合性を保証するバリデーションシステムを作成します。つまり、オブジェクトに格納されるデータは常に特定の条件（特定の型である、正の値であるなど）を満たすようになります。

では、バリデーションシステムの作成を始めましょう。プロジェクトディレクトリに `validate.py` という新しいファイルを作成します。このファイルには、バリデータを実装するクラスが含まれます。

```python
# validate.py

class Validator:
    def __init__(self, name):
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

`validate.py` ファイルでは、まず `Validator` という基底クラスを定義しています。このクラスには、検証対象の属性を識別するために使用される `name` パラメータを受け取る `__init__` メソッドがあります。`check` メソッドはクラスメソッドで、渡された値をそのまま返します。`__set__` メソッドは、オブジェクトの属性が設定されたときに呼び出されるディスクリプタメソッドです。このメソッドは `check` メソッドを呼び出して値を検証し、検証された値をオブジェクトの辞書に格納します。

次に、`Validator` の 3 つのサブクラス `String`、`PositiveInteger`、`PositiveFloat` を定義しています。これらのサブクラスはそれぞれ、特定のバリデーションチェックを実行するために `check` メソッドをオーバーライドしています。`String` クラスは値が文字列であるかをチェックし、`PositiveInteger` クラスは値が正の整数であるかをチェックし、`PositiveFloat` クラスは値が正の数（整数または浮動小数点数）であるかをチェックします。

バリデータが定義できたので、これらのバリデータを使用するように `Stock` クラスを修正しましょう。`stock_with_validators.py` という新しいファイルを作成し、`validate.py` ファイルからバリデータをインポートします。

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

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

`stock_with_validators.py` ファイルでは、`Stock` クラスを定義し、バリデータをクラス属性として使用しています。これは、`Stock` オブジェクトの属性が設定されるたびに、対応するバリデータの `__set__` メソッドが呼び出されて値が検証されることを意味します。`__init__` メソッドは `Stock` オブジェクトの属性を初期化し、`cost`、`sell`、`__repr__` メソッドは追加の機能を提供します。

では、バリデータベースの `Stock` クラスをテストしましょう。ターミナルを開き、プロジェクトディレクトリに移動し、対話モードで `stock_with_validators.py` ファイルを実行します。

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Python インタープリタが起動したら、バリデーションシステムをテストするためのいくつかのコマンドを試してみましょう。

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

テストコードでは、まず有効な値で `Stock` オブジェクトを作成し、その属性を印刷して正しく設定されていることを確認します。次に、`shares` 属性を有効な値に変更し、再度印刷して変更が反映されていることを確認します。最後に、`shares` 属性を無効な値（文字列と負の数）に設定し、バリデータによって発生する例外をキャッチします。

コードがかなりクリーンになったことに注目してください。`Stock` クラスはもはやすべてのプロパティメソッドを実装する必要がなくなりました。バリデータがすべての型チェックと制約を処理します。

ディスクリプタを使用することで、任意のクラス属性に適用できる再利用可能なバリデーションシステムを作成することができました。これは、アプリケーション全体でデータの整合性を維持するための強力なパターンです。
