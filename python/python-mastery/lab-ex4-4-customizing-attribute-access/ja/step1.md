# 属性制御のための `__setattr__` の理解

Python には、オブジェクトの属性のアクセスと変更方法をカスタマイズできる特殊メソッドがあります。その中でも重要なメソッドの 1 つが `__setattr__()` です。このメソッドは、オブジェクトの属性に値を割り当てようとするたびに機能します。属性の割り当てプロセスを細かく制御することができます。

## `__setattr__` とは何ですか？

`__setattr__(self, name, value)` メソッドは、すべての属性割り当てのインターセプターとして機能します。`obj.attr = value` のような単純な割り当て文を書くとき、Python は直接値を割り当てるだけではありません。代わりに、内部的に `obj.__setattr__("attr", value)` を呼び出します。このメカニズムにより、属性割り当て時に何が起こるべきかを決定する力が与えられます。

では、`__setattr__` を使用して、クラスに設定できる属性を制限する実際の例を見てみましょう。

### ステップ 1: 新しいファイルを作成する

まず、WebIDE で新しいファイルを開きます。「File」メニューをクリックしてから「New File」を選択することで行えます。このファイルに `restricted_stock.py` という名前を付け、`/home/labex/project` ディレクトリに保存します。このファイルには、属性割り当てを制御するために `__setattr__` を使用するクラス定義が含まれます。

### ステップ 2: `restricted_stock.py` にコードを追加する

`restricted_stock.py` ファイルに次のコードを追加します。このコードは `RestrictedStock` クラスを定義します。

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

`__init__` メソッドでは、`name`、`shares`、`price` 属性でオブジェクトを初期化します。`__setattr__` メソッドは、割り当てられる属性名が許可された属性のセット (`name`、`shares`、`price`) に含まれているかどうかを確認します。含まれていない場合は、`AttributeError` を発生させます。属性が許可されている場合は、親クラスの `__setattr__` メソッドを使用して実際に属性を設定します。

### ステップ 3: テストファイルを作成する

`test_restricted.py` という新しいファイルを作成し、次のコードを追加します。このコードは `RestrictedStock` クラスの機能をテストします。

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

このコードでは、まず `RestrictedStock` クラスをインポートします。次に、クラスのインスタンスを作成します。既存の属性にアクセスするテスト、既存の属性を変更するテスト、最後に無効な属性を設定して `__setattr__` メソッドが期待どおりに機能するかを確認します。

### ステップ 4: テストファイルを実行する

WebIDE でターミナルを開き、次のコマンドを実行して `test_restricted.py` ファイルを実行します。

```bash
cd /home/labex/project
python3 test_restricted.py
```

これらのコマンドを実行した後、次のような出力が表示されるはずです。

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## 動作原理

`RestrictedStock` クラスの `__setattr__` メソッドは次の手順で動作します。

1. まず、属性名が許可されたセット (`name`、`shares`、`price`) に含まれているかどうかを確認します。
2. 属性名が許可されたセットに含まれていない場合は、`AttributeError` を発生させます。これにより、不要な属性の割り当てが防止されます。
3. 属性が許可されている場合は、`super().__setattr__()` を使用して実際に属性を設定します。これにより、許可された属性に対して通常の属性割り当てプロセスが行われることが保証されます。

このメソッドは、前の例で見た `__slots__` を使用するよりも柔軟です。`__slots__` はメモリ使用量を最適化し、属性を制限することができますが、継承を使用する際に制限があり、他の Python 機能と競合する可能性があります。私たちの `__setattr__` アプローチは、それらの制限の一部を回避しながら、属性割り当てに対して同様の制御を提供します。
