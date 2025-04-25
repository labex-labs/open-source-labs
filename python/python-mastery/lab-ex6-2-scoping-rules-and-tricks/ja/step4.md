# 構造体における高度な初期化の実装

私たちは、関数の引数にアクセスするための 2 つの強力なテクニックを学びました。ここでは、これらのテクニックを使って `Structure` クラスを更新します。まず、なぜこれを行うのかを理解しましょう。これらのテクニックにより、特にさまざまなタイプの引数を扱う際に、クラスがより柔軟で使いやすくなります。

コードエディタで `structure.py` ファイルを開きます。ターミナルで次のコマンドを実行することでこれを行えます。`cd` コマンドはディレクトリをプロジェクトフォルダに変更し、`code` コマンドはコードエディタで `structure.py` ファイルを開きます。

```bash
cd ~/project
code structure.py
```

ファイルの内容を次のコードに置き換えます。このコードは、いくつかのメソッドを持つ `Structure` クラスを定義しています。それぞれの部分を見て、何を行っているかを理解しましょう。

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

このコードで行ったことは次の通りです。

1. 古い `__init__()` メソッドを削除しました。サブクラスが独自の `__init__` メソッドを定義するため、古いメソッドはもう必要ありません。
2. 新しい `_init()` 静的メソッドを追加しました。このメソッドはフレーム調査を使用して、すべてのパラメータを自動的に捕捉して属性として設定します。フレーム調査により、呼び出し元のメソッドのローカル変数にアクセスできます。
3. `__repr__()` メソッドを残しました。このメソッドは、オブジェクトの適切な文字列表現を提供し、デバッグや表示に役立ちます。
4. `__setattr__()` メソッドを追加しました。このメソッドは属性の検証を行い、オブジェクトに設定できるのは有効な属性のみであることを保証します。

次に、`Stock` クラスを更新しましょう。次のコマンドを使って `stock.py` ファイルを開きます。

```bash
code stock.py
```

その内容を次のコードに置き換えます。

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

ここでの重要な変更点は、`__init__` メソッドが各属性を手動で設定する代わりに `self._init()` を呼び出すようになったことです。`_init()` メソッドはフレーム調査を使用して、すべてのパラメータを自動的に捕捉して属性として設定します。これにより、コードがより簡潔で保守しやすくなります。

ユニットテストを実行して、私たちの実装をテストしましょう。ユニットテストは、コードが期待どおりに動作することを確認するのに役立ちます。ターミナルで次のコマンドを実行します。

```bash
cd ~/project
python3 teststock.py
```

以前は失敗していたキーワード引数のテストを含め、すべてのテストが合格するはずです。これは、私たちの実装が正しく動作していることを意味します。

`Stock` クラスのヘルプドキュメントも確認しましょう。ヘルプドキュメントは、クラスとそのメソッドに関する情報を提供します。ターミナルで次のコマンドを実行します。

```bash
python3 -c "from stock import Stock; help(Stock)"
```

これで、`__init__` メソッドの適切なシグネチャが表示され、すべてのパラメータ名が示されるはずです。これにより、他の開発者がクラスの使い方を理解しやすくなります。

最後に、キーワード引数が期待どおりに動作することを対話的にテストしましょう。ターミナルで次のコマンドを実行します。

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

指定された属性で `Stock` オブジェクトが適切に作成されているのが見えるはずです。これにより、クラスの初期化システムがキーワード引数をサポートしていることが確認されます。

この実装により、次のような、はるかに柔軟で使いやすいクラスの初期化システムを実現しました。

1. ドキュメントに適切な関数シグネチャを保持し、開発者がクラスの使い方を理解しやすくします。
2. 位置引数とキーワード引数の両方をサポートし、オブジェクトを作成する際により柔軟性を提供します。
3. サブクラスで必要な定型コードを最小限に抑え、書くコードの量を減らします。
