# メソッド引数検証の追加

Python では、堅牢なコードを作成する上でデータの検証は重要な部分です。このセクションでは、メソッド引数を自動的に検証することで、検証をさらに一歩進めます。`validate.py` ファイルにはすでに `@validated` デコレータが含まれています。Python のデコレータは、別の関数を変更できる特別な関数です。ここでの `@validated` デコレータは、関数引数を注釈と比較してチェックできます。Python の注釈は、関数パラメータと戻り値にメタデータを追加する方法です。

コードを変更して、このデコレータを注釈付きのメソッドに適用しましょう。

1. まず、`validated` デコレータがどのように機能するかを理解する必要があります。エディタで `validate.py` ファイルを開いて確認してください。

`validated` デコレータは、関数注釈を使用して引数を検証します。関数を実行する前に、注釈付きの各パラメータに対してバリデータクラスのインスタンスを作成し、`validate` メソッドを呼び出して引数をチェックします。たとえば、引数が `PositiveInteger` で注釈付けされている場合、デコレータは `PositiveInteger` インスタンスを作成し、渡された値が実際に正の整数であることを検証します。検証が失敗した場合、すべてのエラーを収集し、詳細なエラーメッセージとともに `TypeError` を発生させます。

2. 次に、`structure.py` の `validate_attributes` 関数を変更して、注釈付きのメソッドを `validated` デコレータでラップします。これは、クラス内の注釈付きのメソッドはすべて、引数が自動的に検証されることを意味します。エディタで `structure.py` ファイルを開きます。

3. `validate_attributes` 関数を更新します。

```python
def validate_attributes(cls):
    """
    クラスデコレータで、以下の処理を行います。
    1. Validator インスタンスを抽出し、_fields および_types リストを構築します。
    2. 注釈付きのメソッドに@validated デコレータを適用します。
    """
    # validated デコレータをインポートします
    from validate import validated

    # バリデータディスクリプタを処理します
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # バリデータ名に基づいて _fields を設定します
    cls._fields = [val.name for val in validators]

    # バリデータの expected_types に基づいて _types を設定します
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # 注釈付きのメソッドに @validated デコレータを適用します
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # 初期化メソッドを作成します
    cls.create_init()

    return cls
```

この更新された関数は、次のことを行います。

1. 以前と同様にバリデータディスクリプタを処理します。バリデータディスクリプタは、クラス属性の検証ルールを定義するために使用されます。
2. クラス内のすべての注釈付きメソッドを見つけます。注釈はメソッドパラメータに追加され、引数の期待される型を指定します。
3. これらのメソッドに `@validated` デコレータを適用します。これにより、これらのメソッドに渡される引数が注釈に従って検証されることが保証されます。

4. これらの変更を行った後、ファイルを保存します。ファイルを保存することは、変更が保存され、後で使用できることを確認するために重要です。

5. 次に、`Stock` クラスの `sell` メソッドを更新して注釈を含めましょう。注釈は、引数の期待される型を指定するのに役立ち、これは `@validated` デコレータによって検証に使用されます。エディタで `stock.py` ファイルを開きます。

6. `sell` メソッドを更新して型注釈を含めます。

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

重要な変更は、`nshares` パラメータに `: PositiveInteger` を追加することです。これにより、Python（および `@validated` デコレータ）は `PositiveInteger` バリデータを使用してこの引数を検証するようになります。したがって、`sell` メソッドを呼び出すとき、`nshares` 引数は正の整数である必要があります。

7. すべてがまだ機能することを確認するために、再度テストを実行します。テストを実行することは、変更によって既存の機能が壊れていないことを確認するための良い方法です。

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

8. 新しい引数検証をテストしましょう。検証が期待どおりに機能するかどうかを確認するために、有効な引数と無効な引数で `sell` メソッドを呼び出してみます。

```bash
cd ~/project
python3 -c "
from stock import Stock
s = Stock('GOOG', 100, 490.1)
s.sell(25)
print(s)
try:
    s.sell(-25)
except Exception as e:
    print(f'Error: {e}')
"
```

次のような出力が表示されるはずです。

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: nshares must be >= 0
```

これは、メソッド引数検証が機能していることを示しています！`sell(25)` への最初の呼び出しは、`25` が正の整数であるため成功します。しかし、`sell(-25)` への 2 回目の呼び出しは、`-25` が正の整数ではないため失敗します。

これで、次のための完全なシステムが実装されました。

1. ディスクリプタを使用したクラス属性の検証。ディスクリプタは、クラス属性の検証ルールを定義するために使用されます。
2. クラスデコレータを使用したフィールド情報の自動収集。クラスデコレータは、フィールド情報の収集のように、クラスの動作を変更できます。
3. 行データをインスタンスに変換。これは、外部ソースからのデータを扱う場合に役立ちます。
4. 注釈を使用したメソッド引数の検証。注釈は、検証のために引数の期待される型を指定するのに役立ちます。

これは、Python でディスクリプタとデコレータを組み合わせることで、表現力豊かで自己検証型のクラスを作成できることを示しています。
