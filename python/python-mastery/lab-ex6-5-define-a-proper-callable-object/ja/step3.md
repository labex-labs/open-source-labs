# 関数アノテーションを用いた型検証の実装

Python では、関数のパラメータに型アノテーションを追加することができます。これらのアノテーションは、パラメータと関数の戻り値の期待されるデータ型を示す方法として機能します。デフォルトでは実行時に型を強制しませんが、検証目的で使用することができます。

例を見てみましょう。

```python
def add(x: int, y: int) -> int:
    return x + y
```

このコードでは、`x: int` と `y: int` は、パラメータ `x` と `y` が整数であるべきことを示しています。末尾の `-> int` は、関数 `add` が整数を返すことを示しています。これらの型アノテーションは、関数の `__annotations__` 属性に格納されます。この属性は、パラメータ名をそのアノテーションされた型にマッピングする辞書です。

では、これらの型アノテーションを検証に使用するように、`ValidatedFunction` クラスを拡張しましょう。これを行うには、Python の `inspect` モジュールを使用する必要があります。このモジュールは、モジュール、クラス、メソッド、関数などのライブオブジェクトに関する情報を取得するための便利な関数を提供します。今回の場合、関数の引数を対応するパラメータ名とマッチングさせるために使用します。

まず、`validate.py` ファイルの `ValidatedFunction` クラスを変更する必要があります。以下のコマンドを使用してこのファイルを開くことができます。

```bash
code /home/labex/project/validate.py
```

既存の `ValidatedFunction` クラスを以下の改良版に置き換えます。

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

この改良版は以下のようなことを行います。

1. `inspect.signature()` を使用して、関数のパラメータに関する情報（名前、デフォルト値、アノテーションされた型など）を取得します。
2. シグネチャの `bind()` メソッドを使用して、提供された引数を対応するパラメータ名とマッチングさせます。これにより、各引数を関数内の正しいパラメータに関連付けることができます。
3. 各引数をその型アノテーション（存在する場合）と照合します。アノテーションが見つかった場合、アノテーションからバリデータクラスを取得し、`check()` メソッドを使用して検証を適用します。
4. 最後に、検証された引数で元の関数を呼び出します。

では、型アノテーションにバリデータクラスを使用するいくつかの関数で、この拡張された `ValidatedFunction` クラスをテストしましょう。以下のコマンドを使用して `test_validation.py` ファイルを開きます。

```bash
code /home/labex/project/test_validation.py
```

ファイルに以下のコードを追加します。

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

このコードでは、型アノテーション `name: String` と `times: Integer` を持つ `greet` 関数を定義しています。これは、`name` パラメータは `String` クラスを使用して検証され、`times` パラメータは `Integer` クラスを使用して検証されることを意味します。その後、`greet` 関数を `ValidatedFunction` クラスでラップして、型検証を有効にします。

3 つのテストケースを実行します。有効な呼び出し、`name` の型が間違っている無効な呼び出し、`times` の型が間違っている無効な呼び出しです。各呼び出しは、検証中に発生する可能性のある `TypeError` 例外をキャッチするために `try-except` ブロックでラップされています。

テストファイルを実行するには、以下のコマンドを使用します。

```bash
python3 /home/labex/project/test_validation.py
```

以下のような出力が表示されるはずです。

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

この出力は、`ValidatedFunction` 呼び出し可能オブジェクトが、関数アノテーションに基づいて型検証を実施していることを示しています。間違った型の引数を渡すと、バリデータクラスがエラーを検出し、`TypeError` を発生させます。これにより、関数が正しいデータ型で呼び出されることを保証でき、バグを防ぎ、コードをより堅牢にすることができます。
