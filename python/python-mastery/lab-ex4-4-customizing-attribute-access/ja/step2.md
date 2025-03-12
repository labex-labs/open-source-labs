# プロキシを使った読み取り専用オブジェクトの作成

このステップでは、Python で非常に有用なパターンであるプロキシクラスを探索します。プロキシクラスを使うと、既存のオブジェクトを利用し、その元のコードを変更することなく振る舞いを変えることができます。これは、オブジェクトに特別なラッパーをかぶせて、新しい機能や制限を追加するようなものです。

## プロキシとは何ですか？

プロキシは、あなたと別のオブジェクトの間に立つオブジェクトです。元のオブジェクトと同じ関数とプロパティのセットを持っていますが、追加のことができます。たとえば、オブジェクトにアクセスできる人を制御したり、アクションの記録（ロギング）を行ったり、他の有用な機能を追加したりすることができます。

では、読み取り専用プロキシを作成しましょう。この種のプロキシは、オブジェクトの属性を変更できないようにします。

### ステップ 1: 読み取り専用プロキシクラスを作成する

まず、読み取り専用プロキシを定義する Python ファイルを作成する必要があります。

1. `/home/labex/project` ディレクトリに移動します。
2. このディレクトリに `readonly_proxy.py` という名前の新しいファイルを作成します。
3. `readonly_proxy.py` ファイルを開き、次のコードを追加します。

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

このコードでは、`ReadonlyProxy` クラスが定義されています。`__init__` メソッドは、ラップするオブジェクトを保存します。`__setattr__` メソッドを呼び出さないように、`self.__dict__` を使って直接保存します。`__getattr__` メソッドは、プロキシの属性にアクセスしようとするときに使われます。属性アクセスの要求をラップされたオブジェクトに渡します。`__setattr__` メソッドは、属性を変更しようとするときに呼び出されます。変更を防ぐためにエラーを発生させます。

### ステップ 2: テストファイルを作成する

次に、読み取り専用プロキシがどのように動作するかを確認するためのテストファイルを作成します。

1. 同じ `/home/labex/project` ディレクトリに `test_readonly.py` という名前の新しいファイルを作成します。
2. `test_readonly.py` ファイルに次のコードを追加します。

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

このテストコードでは、まず通常の `Stock` オブジェクトを作成し、その情報を表示します。次に、その属性の 1 つを変更し、更新された情報を表示します。次に、`Stock` オブジェクトの読み取り専用プロキシを作成し、その情報を表示します。最後に、読み取り専用プロキシを変更しようとし、エラーが発生することを期待します。

### ステップ 3: テストスクリプトを実行する

プロキシクラスとテストファイルを作成した後、テストスクリプトを実行して結果を確認する必要があります。

1. ターミナルを開き、次のコマンドを使って `/home/labex/project` ディレクトリに移動します。

```bash
cd /home/labex/project
```

2. 次のコマンドを使ってテストスクリプトを実行します。

```bash
python3 test_readonly.py
```

次のような出力が表示されるはずです。

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## プロキシの動作原理

`ReadonlyProxy` クラスは、読み取り専用機能を実現するために 2 つの特殊メソッドを使用しています。

1. `__getattr__(self, name)`: このメソッドは、Python が通常の方法で属性を見つけられないときに呼び出されます。`ReadonlyProxy` クラスでは、`getattr()` 関数を使って属性アクセスの要求をラップされたオブジェクトに渡します。したがって、プロキシの属性にアクセスしようとすると、実際にはラップされたオブジェクトから属性を取得します。

2. `__setattr__(self, name, value)`: このメソッドは、属性に値を割り当てようとするときに呼び出されます。この実装では、`AttributeError` を発生させて、プロキシの属性に対する変更を阻止します。

3. `__init__` メソッドでは、`self.__dict__` を直接変更してラップされたオブジェクトを保存します。通常の方法でオブジェクトを割り当てると、`__setattr__` メソッドが呼び出されてエラーが発生するため、これは重要です。

このプロキシパターンにより、既存のオブジェクトの元のクラスを変更することなく、読み取り専用のレイヤーを追加することができます。プロキシオブジェクトはラップされたオブジェクトのように振る舞いますが、変更を許可しません。
