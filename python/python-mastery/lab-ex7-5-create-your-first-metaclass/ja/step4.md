# メタクラスの継承を探索する

メタクラスには興味深い特性があります。それは「粘着性」があるということです。つまり、あるクラスがメタクラスを使用すると、その継承階層にあるすべてのサブクラスも同じメタクラスを使用することになります。言い換えると、メタクラスの特性は継承チェーンを通じて伝播します。

実際にこれを見てみましょう。

1. まず、`mymeta.py` ファイルを開きます。このファイルの末尾に新しいクラスを追加します。このクラスは `MyStock` という名前で、`Stock` クラスを継承します。`__init__` メソッドはオブジェクトの属性を初期化するために使用され、`super().__init__` を使って親クラスの `__init__` メソッドを呼び出し、共通の属性を初期化します。`info` メソッドは株式に関する情報を含む書式付きの文字列を返すために使用されます。以下のコードを追加します。

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. コードを追加したら、`mymeta.py` ファイルを保存します。ファイルを保存することで、行った変更が保存され、後で使用できるようになります。

3. 次に、`test_inheritance.py` という新しいファイルを作成して、メタクラスの継承動作をテストします。このファイルでは、`mymeta.py` ファイルから `MyStock` クラスをインポートします。その後、`MyStock` クラスのインスタンスを作成し、そのメソッドを呼び出し、結果を出力して、メタクラスが継承を通じてどのように動作するかを確認します。`test_inheritance.py` に以下のコードを追加します。

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. 最後に、`test_inheritance.py` ファイルを実行して、メタクラスが継承を通じてどのように動作するかを確認します。ターミナルを開き、`test_inheritance.py` ファイルがあるディレクトリに移動して、以下のコマンドを実行します。

```bash
python3 test_inheritance.py
```

以下のような出力が表示されるはずです。

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

`MyStock` クラスに明示的にメタクラスを指定していないにもかかわらず、メタクラスが適用されていることに注意してください。これは、メタクラスが継承を通じてどのように伝播するかを明確に示しています。

## メタクラスの実用的な用途

この例では、メタクラスは単にクラスに関する情報を出力するだけです。しかし、メタクラスは実際のプログラミングにおいて多くの実用的な用途があります。

1. **検証**: メタクラスを使用して、クラスが必要なメソッドや属性を持っているかどうかを確認することができます。これにより、クラスが使用される前に特定の基準を満たしていることを保証するのに役立ちます。
2. **登録**: メタクラスはクラスを自動的にレジストリに登録することができます。特定のタイプのすべてのクラスを追跡する必要がある場合に便利です。
3. **インターフェースの強制**: クラスが必要なインターフェースを実装していることを保証するために使用できます。これにより、コードの一貫した構造を維持するのに役立ちます。
4. **アスペクト指向プログラミング**: メタクラスはメソッドに振る舞いを追加することができます。たとえば、メソッドのコードを直接変更することなく、ロギングやパフォーマンス監視を追加することができます。
5. **ORM システム**: Django や SQLAlchemy のようなオブジェクトリレーショナルマッピング (ORM) システムでは、メタクラスを使用してクラスをデータベーステーブルにマッピングします。これにより、アプリケーション内のデータベース操作が簡素化されます。

メタクラスは非常に強力ですが、控えめに使用する必要があります。Python のコードの美しさを表現した「Python の禅」の著者である Tim Peters が言ったように、「メタクラスは 99% のユーザーが心配する必要のない魔法です。」
