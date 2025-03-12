# 基本的な呼び出し可能オブジェクトの作成

Python では、呼び出し可能オブジェクトとは、関数のように使用できるオブジェクトです。関数を呼び出すときのように、オブジェクトの後に括弧を付けて「呼び出す」ことができるものと考えることができます。Python のクラスを呼び出し可能オブジェクトのように振る舞わせるには、`__call__` という特殊メソッドを実装する必要があります。このメソッドは、オブジェクトに括弧を付けて使用すると自動的に呼び出され、関数を呼び出すときと同じように動作します。

まず、`validate.py` ファイルを変更しましょう。このファイルに `ValidatedFunction` という新しいクラスを追加します。このクラスが私たちの呼び出し可能オブジェクトになります。コードエディタでファイルを開くには、ターミナルで以下のコマンドを実行します。

```bash
code /home/labex/project/validate.py
```

ファイルが開いたら、末尾までスクロールして以下のコードを追加します。

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

このコードが何をするか解説しましょう。`ValidatedFunction` クラスには `__init__` メソッドがあり、これはコンストラクタです。このクラスのインスタンスを作成するときに、関数を渡します。この関数は、インスタンスの属性として `self.func` という名前で保存されます。

`__call__` メソッドが、このクラスを呼び出し可能にする重要な部分です。`ValidatedFunction` クラスのインスタンスを呼び出すと、この `__call__` メソッドが実行されます。以下は、その動作をステップごとに説明したものです。

1. どの関数が呼び出されているかを示すメッセージを出力します。これはデバッグや動作の理解に役立ちます。
2. インスタンスを呼び出したときに渡された引数で、`self.func` に保存されている関数を呼び出します。`*args` と `**kwargs` を使用することで、任意の数の位置引数とキーワード引数を渡すことができます。
3. 関数呼び出しの結果を返します。

では、この `ValidatedFunction` クラスをテストしましょう。テストコードを書くために、`test_callable.py` という新しいファイルを作成します。コードエディタでこの新しいファイルを開くには、以下のコマンドを実行します。

```bash
code /home/labex/project/test_callable.py
```

`test_callable.py` ファイルに以下のコードを追加します。

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

このコードでは、まず `validate.py` ファイルから `ValidatedFunction` クラスをインポートします。次に、2 つの数値を受け取り、その合計を返す `add` という簡単な関数を定義します。

`ValidatedFunction` クラスのインスタンスを作成し、`add` 関数を渡します。これにより、`add` 関数が `ValidatedFunction` インスタンスの中に「ラップ」されます。

その後、ラップされた関数を 2 回呼び出します。1 回目は引数 `2` と `3` で、2 回目は `10` と `20` です。ラップされた関数を呼び出すたびに、`ValidatedFunction` クラスの `__call__` メソッドが呼び出され、それが元の `add` 関数を呼び出します。

テストコードを実行するには、ターミナルで以下のコマンドを実行します。

```bash
python3 /home/labex/project/test_callable.py
```

以下のような出力が表示されるはずです。

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

この出力は、私たちの呼び出し可能オブジェクトが期待通りに動作していることを示しています。`validated_add(2, 3)` を呼び出すと、実際には `ValidatedFunction` クラスの `__call__` メソッドが呼び出され、それが元の `add` 関数を呼び出します。

現時点では、`ValidatedFunction` クラスはメッセージを出力し、呼び出しを元の関数に渡すだけです。次のステップでは、このクラスを改良して、関数のアノテーションに基づいた型検証を行うようにします。
