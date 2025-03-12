# バリデータ型の収集

Python では、バリデータはデータが特定の基準を満たしていることを保証するのに役立つクラスです。この実験の最初のタスクは、基本の `Validator` クラスを変更して、そのすべてのサブクラスを収集できるようにすることです。なぜこれが必要なのでしょうか？すべてのバリデータサブクラスを収集することで、すべてのバリデータ型を含む名前空間を作成できます。後で、この名前空間を `Structure` クラスに注入します。これにより、さまざまなバリデータを管理および使用しやすくなります。

では、コードの作業を始めましょう。`validate.py` ファイルを開きます。ターミナルで次のコマンドを使用して開くことができます。

```bash
code validate.py
```

ファイルが開いたら、`Validator` クラスにクラスレベルの辞書と `__init_subclass__()` メソッドを追加する必要があります。クラスレベルの辞書はすべてのバリデータサブクラスを格納するために使用され、`__init_subclass__()` メソッドは Python の特殊メソッドで、現在のクラスのサブクラスが定義されるたびに呼び出されます。

次のコードを `Validator` クラスの定義の直後に追加します。

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

コードを追加した後、変更後の `Validator` クラスは次のようになります。

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

これで、`String` や `PositiveInteger` のような新しいバリデータ型が定義されるたびに、Python は自動的に `__init_subclass__()` メソッドを呼び出します。このメソッドは、新しいバリデータサブクラスをクラス名をキーとして `validators` 辞書に追加します。

コードが機能するかテストしましょう。`validators` 辞書の内容を確認するための簡単な Python スクリプトを作成します。ターミナルで次のコマンドを実行できます。

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

すべてが正しく機能する場合、次のような出力が表示され、すべてのバリデータ型とそれに対応するクラスが表示されます。

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

これで、すべてのバリデータ型を含む辞書ができました。次のステップでこれを使用してメタクラスを作成します。
