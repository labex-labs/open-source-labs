# メタクラスの使用

ここでは、継承を通じて自作のメタクラスを使用するクラスを作成します。これにより、クラスが定義される際にメタクラスがどのように呼び出されるかを理解することができます。

Python のメタクラスは、他のクラスを作成するクラスです。クラスを定義するとき、Python はメタクラスを使ってそのクラスオブジェクトを構築します。継承を使用することで、クラスが使用するメタクラスを指定することができます。

1. `mymeta.py` を開き、ファイルの末尾に以下のコードを追加します。

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

ここでは、`myobject` を継承した `Stock` クラスを定義しています。`__init__` メソッドは Python クラスの特殊メソッドです。クラスのオブジェクトが作成されるときに呼び出され、オブジェクトの属性を初期化するために使用されます。`cost` メソッドは株式の総コストを計算し、`sell` メソッドは株式の数を減らします。

2. Ctrl + S を押してファイルを保存します。ファイルを保存することで、行った変更が保存され、後で実行できるようになります。

3. では、ファイルを実行して何が起こるかを見てみましょう。WebIDE でターミナルを開き、以下のコマンドを実行します。

```bash
cd /home/labex/project
python3 mymeta.py
```

`cd` コマンドは現在の作業ディレクトリを `/home/labex/project` に変更し、`python3 mymeta.py` は Python スクリプト `mymeta.py` を実行します。

以下のような出力が表示されるはずです。

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

この出力は、`myobject` クラスと `Stock` クラスが作成される際に自作のメタクラスが呼び出されていることを示しています。以下の点に注目してください。

- `Stock` の場合、基底クラスに `myobject` が含まれています。なぜなら、`Stock` は `myobject` を継承しているからです。
- 属性のリストには、定義したすべてのメソッド (`__init__`, `cost`, `sell`) といくつかのデフォルト属性が含まれています。

4. `Stock` クラスと対話してみましょう。以下の内容で `test_stock.py` という新しいファイルを作成します。

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

このコードでは、`mymeta` モジュールから `Stock` クラスをインポートしています。その後、`Stock` クラスのインスタンス `apple` を作成します。`Stock` クラスのメソッドを使用して、株式に関する情報を出力し、総コストを計算し、いくつかの株式を売却し、更新された情報を出力します。

5. このファイルを実行して `Stock` クラスをテストします。

```bash
python3 test_stock.py
```

以下のような出力が表示されるはずです。

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

メタクラスに関する情報が最初に出力され、その後にテストスクリプトの出力が表示されることに注意してください。これは、クラスが定義される際にメタクラスが呼び出されるためであり、これはテストスクリプトのコードが実行される前に行われます。
