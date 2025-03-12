# データ構造としてのクロージャ

Python では、クロージャ (Closure) はデータをカプセル化する強力な方法を提供します。カプセル化とは、データを非公開に保ち、それへのアクセスを制御することを意味します。クロージャを使用すると、クラスやグローバル変数を使用せずに、非公開データを管理および変更する関数を作成できます。グローバル変数はコード内のどこからでもアクセスおよび変更できるため、予期しない動作を引き起こす可能性があります。一方、クラスはより複雑な構造を必要とします。クロージャは、データのカプセル化においてよりシンプルな代替手段を提供します。

この概念を実証するために、`counter.py` という名前のファイルを作成しましょう。

1. WebIDE を開き、`/home/labex/project` ディレクトリに `counter.py` という名前の新しいファイルを作成します。ここに、クロージャベースのカウンタを定義するコードを記述します。

2. ファイルに以下のコードを追加します。

```python
def counter(value):
    """
    Create a counter with increment and decrement functions.

    Args:
        value: Initial value of the counter

    Returns:
        Two functions: one to increment the counter, one to decrement it
    """
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

このコードでは、`counter()` という関数を定義しています。この関数は初期の `value` を引数として受け取ります。`counter()` 関数の内部では、2 つの内部関数 `incr()` と `decr()` を定義しています。これらの内部関数は同じ `value` 変数にアクセスできます。`nonlocal` キーワードは、Python に対して外側のスコープ（`counter()` 関数）の `value` 変数を変更したいことを伝えるために使用されます。`nonlocal` キーワードがない場合、Python は内部関数内に新しいローカル変数を作成し、外側のスコープの `value` を変更するのではなくなります。

3. これを実際に動作させるためのテストファイルを作成しましょう。以下の内容で `test_counter.py` という名前の新しいファイルを作成します。

```python
from counter import counter

# Create a counter starting at 0
up, down = counter(0)

# Increment the counter several times
print("Incrementing the counter:")
print(up())  # Should print 1
print(up())  # Should print 2
print(up())  # Should print 3

# Decrement the counter
print("\nDecrementing the counter:")
print(down())  # Should print 2
print(down())  # Should print 1
```

このテストファイルでは、まず `counter.py` ファイルから `counter()` 関数をインポートします。次に、`counter(0)` を呼び出して 0 から始まるカウンタを作成し、返された関数を `up` と `down` にアンパックします。その後、`up()` 関数を何度か呼び出してカウンタを増やし、結果を出力します。その後、`down()` 関数を呼び出してカウンタを減らし、結果を出力します。

4. ターミナルで以下のコマンドを実行してテストファイルを実行します。

```bash
python3 test_counter.py
```

以下の出力が表示されるはずです。

```
Incrementing the counter:
1
2
3

Decrementing the counter:
2
1
```

ここではクラス定義が関与していないことに注意してください。`up()` と `down()` 関数は、グローバル変数でもインスタンス属性でもない共有値を操作しています。この値はクロージャ内に格納されており、`counter()` が返す関数のみがアクセスできます。

これは、クロージャがデータ構造としてどのように使用できるかの例です。閉じ込められた変数 `value` は関数呼び出し間で維持され、それにアクセスする関数に対して非公開です。これは、コードの他の部分がこの `value` 変数に直接アクセスまたは変更できないことを意味し、一定のレベルのデータ保護を提供します。
