# スタックフレームの調査を探索する

これまで使用してきた `_init(locals())` のアプローチは機能的ですが、欠点があります。`__init__` メソッドを定義するたびに、明示的に `locals()` を呼び出す必要があります。これは、特に複数のクラスを扱う場合に少し面倒になることがあります。幸いなことに、スタックフレームの調査を使用することで、コードをよりクリーンで効率的にすることができます。このテクニックを使用すると、明示的に `locals()` を呼び出すことなく、呼び出し元のローカル変数に自動的にアクセスすることができます。

Python インタープリターでこのテクニックを探索し始めましょう。まず、ターミナルを開き、プロジェクトディレクトリに移動します。次に、Python インタープリターを起動します。これは、次のコマンドを実行することで行うことができます。

```bash
cd ~/project
python3
```

Python インタープリターに入ったら、`sys` モジュールをインポートする必要があります。`sys` モジュールは、Python インタープリターによって使用または維持されるいくつかの変数にアクセスするための機能を提供します。これを使用して、スタックフレームの情報にアクセスします。

```python
import sys
```

次に、`_init()` 関数の改良版を定義します。この新しいバージョンでは、呼び出し元のフレームに直接アクセスするため、明示的に `locals()` を渡す必要がなくなります。

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

このコードでは、`sys._getframe(1)` が呼び出し元の関数のフレームオブジェクトを取得します。引数の `1` は、呼び出しスタックの 1 レベル上を指します。フレームオブジェクトを取得したら、`frame.f_locals` を使用してそのローカル変数にアクセスできます。これにより、呼び出し元のスコープ内のすべてのローカル変数の辞書が得られます。その後、`self` 変数を抽出し、残りの変数を `self` オブジェクトの属性として設定します。

では、この新しい `_init()` 関数を `Stock` クラスの新しいバージョンでテストしましょう。

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

ご覧のとおり、`__init__` メソッドはもはや明示的に `locals()` を渡す必要がありません。これにより、呼び出し元の観点からコードがクリーンで読みやすくなります。

### スタックフレームの調査の仕組み

`sys._getframe(1)` を呼び出すと、Python は呼び出し元の実行フレームを表すフレームオブジェクトを返します。引数の `1` は、「現在のフレームから 1 レベル上」（呼び出し元の関数）を意味します。

フレームオブジェクトには、実行コンテキストに関する重要な情報が含まれています。これには、現在実行中の関数、その関数内のローカル変数、および現在実行中の行番号が含まれます。

`frame.f_locals` にアクセスすることで、呼び出し元のスコープ内のすべてのローカル変数の辞書が得られます。これは、そのスコープから直接 `locals()` を呼び出した場合と同様の結果になります。

このテクニックは非常に強力ですが、注意して使用する必要があります。これは一般的に高度な Python の機能と見なされ、Python の通常のスコープ境界を越えるため、少し「魔法のよう」に見えることがあります。

スタックフレームの調査の実験が終了したら、次のコマンドを実行して Python インタープリターを終了できます。

```python
exit()
```
