# 基本的な MutInt クラスの作成

まずは、可変整数型（Mutable Integer）の基本的なクラスを作成しましょう。プログラミングにおいて、クラスはオブジェクトを作成するためのブループリントのようなものです。このステップでは、新しいプリミティブ型の基礎を構築します。プリミティブ型とは、プログラミング言語が提供する基本的なデータ型で、ここでは独自のカスタム型を作成します。

1. WebIDE を開き、`/home/labex/project` ディレクトリに移動します。WebIDE は、コードを記述、編集、実行できる統合開発環境です。このディレクトリに移動することで、すべてのファイルが一箇所に整理され、適切に相互作用できるようになります。

2. セットアップステップで作成された `mutint.py` ファイルを開きます。このファイルは、`MutInt` クラスの定義を記述する場所になります。

3. 次のコードを追加して、基本的な `MutInt` クラスを定義します。

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value
```

`__slots__` 属性は、このクラスが持つことができる属性を定義するために使用されます。属性は、クラスのオブジェクトに属する変数のようなものです。`__slots__` を使用することで、Python に属性を格納するためのよりメモリ効率の良い方法を使用するよう指示します。この場合、`MutInt` クラスは `value` という単一の属性のみを持つことになります。つまり、`MutInt` クラスの各オブジェクトは、整数値という 1 つのデータのみを保持できます。

`__init__` メソッドは、クラスのコンストラクタです。コンストラクタは、クラスのオブジェクトが作成されるときに呼び出される特別なメソッドです。これは `value` パラメータを受け取り、それをインスタンスの `value` 属性に格納します。インスタンスとは、クラスのブループリントから作成された個々のオブジェクトのことです。

クラスを使用する Python スクリプトを作成して、テストしてみましょう。

4. 同じディレクトリに `test_mutint.py` という新しいファイルを作成します。

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

このテストスクリプトでは、まず `mutint.py` ファイルから `MutInt` クラスをインポートします。次に、初期値 3 で `MutInt` クラスのオブジェクトを作成します。初期値を出力し、その後 42 に変更して新しい値を出力します。最後に、`MutInt` オブジェクトに 10 を足そうとしますが、このクラスはまだ加算演算をサポートしていないため、エラーが発生します。

5. ターミナルで次のコマンドを実行して、テストスクリプトを実行します。

```bash
python3 /home/labex/project/test_mutint.py
```

ターミナルは、システムやコードと対話するための様々なコマンドを実行できるコマンドラインインターフェイスです。このコマンドを実行すると、`test_mutint.py` スクリプトが実行されます。

次のような出力が表示されるはずです。

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

`MutInt` クラスは、値を正常に格納して更新することができます。しかし、いくつかの制限があります。

- 印刷するときに見栄えが良くない
- 加算などの数学的演算をサポートしていない
- 比較演算をサポートしていない
- 型変換をサポートしていない

次のステップでは、これらの制限を 1 つずつ解消して、`MutInt` クラスをより本格的なプリミティブ型のように動作させます。
