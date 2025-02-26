# 最初のメタクラスを作成する

`mymeta.py` という名前のファイルを作成し、次のコードを入力します（スライドから）。

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

これを行ったら、`object` ではなく `myobject` から継承するクラスを定義します。たとえば：

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

コードを実行して `Stock` のインスタンスを作成してみましょう。何が起こるか見てみましょう。`Stock` クラスが定義されるときに、`mytype` の `print` 文が一度だけ実行されるはずです。

`Stock` から継承する場合、何が起こりますか？

```python
class MyStock(Stock):
    pass
```

メタクラスがまだ機能していることがわかるはずです。メタクラスは、それが全体的な継承階層に適用されるという点で「粘着性があり」ます。

**考察**

なぜこのようなことをしたいのでしょうか？メタクラスの主な強みは、プログラマにクラスが作成される直前のクラスに関する詳細を把握する能力を与えることです。たとえば、`__new__()` メソッドでは、クラス名、基底クラス、メソッドデータなどのすべての基本的な詳細が与えられます。このデータを調べると、さまざまな種類の診断チェックを行うことができます。もっと大胆であれば、データを変更して、クラス定義が作成されるときにクラス定義に入れられるものを変更することができます。言うまでもなく、恐ろしい悪意のあることがたくさんあります。
