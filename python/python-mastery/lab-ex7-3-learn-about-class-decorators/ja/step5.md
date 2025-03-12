# メソッド引数の検証機能の追加

Pythonにおいて、データの検証は堅牢なコードを書く上で重要な要素です。このセクションでは、メソッドの引数を自動的に検証することで、検証機能をさらに拡張します。`validate.py` ファイルには既に `@validated` デコレータが含まれています。Pythonのデコレータは、他の関数を修飾する特殊な関数です。ここでの `@validated` デコレータは、関数の引数をアノテーションと照らし合わせて検証することができます。Pythonのアノテーションは、関数のパラメータや戻り値にメタデータを追加する方法です。

このデコレータをアノテーション付きのメソッドに適用するようにコードを変更しましょう。

1. まず、`validated` デコレータの動作を理解する必要があります。`validate.py` ファイルを開いて確認します。

```bash
code ~/project/validate.py
```

`validated` デコレータは、関数のアノテーションを使用して引数を検証します。関数を実行する前に、各引数をそのアノテーションの型と照らし合わせてチェックします。たとえば、引数が整数としてアノテーションされている場合、デコレータは渡された値が実際に整数であることを確認します。

2. 次に、`structure.py` の `validate_attributes` 関数を変更して、アノテーション付きのメソッドを `validated` デコレータでラップします。これにより、クラス内のアノテーション付きのメソッドの引数は自動的に検証されます。`structure.py` ファイルを開きます。

```bash
code ~/project/structure.py
```

3. `validate_attributes` 関数を更新します。

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

この更新された関数は以下のことを行います。

1. 以前と同様に、バリデータディスクリプタを処理します。バリデータディスクリプタは、クラス属性の検証ルールを定義するために使用されます。
2. クラス内のアノテーション付きのすべてのメソッドを見つけます。アノテーションは、メソッドのパラメータに追加され、引数の期待される型を指定します。
3. それらのメソッドに `@validated` デコレータを適用します。これにより、これらのメソッドに渡される引数は、そのアノテーションに従って検証されます。

4. これらの変更を加えた後、ファイルを保存します。ファイルを保存することは、変更が保存され、後で使用できるようにするために重要です。

5. 次に、`Stock` クラスの `sell` メソッドを更新して、アノテーションを追加します。アノテーションは、引数の期待される型を指定するのに役立ち、`@validated` デコレータによる検証に使用されます。`stock.py` ファイルを開きます。

```bash
code ~/project/stock.py
```

6. `sell` メソッドを変更して、型アノテーションを追加します。

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

重要な変更点は、`nshares` パラメータに `: PositiveInteger` を追加したことです。これは、Python（および `@validated` デコレータ）に、この引数を `PositiveInteger` バリデータを使用して検証するよう指示します。したがって、`sell` メソッドを呼び出すとき、`nshares` 引数は正の整数でなければなりません。

7. すべてが正常に動作することを確認するために、再度テストを実行します。テストを実行することは、変更によって既存の機能が破壊されていないことを確認する良い方法です。

```bash
cd ~/project
python3 teststock.py
```

すべてのテストが合格するはずです。

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

8. 新しい引数検証機能をテストしましょう。有効な引数と無効な引数で `sell` メソッドを呼び出して、検証が期待通りに動作するかを確認します。

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

以下のような出力が表示されるはずです。

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

これは、メソッド引数の検証が正常に動作していることを示しています！最初の `sell(25)` の呼び出しは成功します。なぜなら、`25` は正の整数だからです。しかし、2回目の `sell(-25)` の呼び出しは失敗します。なぜなら、`-25` は正の整数ではないからです。

これで、以下の完全なシステムを実装しました。

1. ディスクリプタを使用してクラス属性を検証する。ディスクリプタは、クラス属性の検証ルールを定義するために使用されます。
2. クラスデコレータを使用してフィールド情報を自動的に収集する。クラスデコレータは、クラスの動作を変更することができ、たとえばフィールド情報を収集することができます。
3. 行データをインスタンスに変換する。これは、外部ソースからのデータを扱う際に便利です。
4. アノテーションを使用してメソッド引数を検証する。アノテーションは、検証のために引数の期待される型を指定するのに役立ちます。

これは、Pythonでディスクリプタとデコレータを組み合わせて、表現力があり、自己検証可能なクラスを作成する力を示しています。
