# 検証デコレータの作成

このステップでは、より実用的なデコレータを作成します。Python のデコレータ (Decorator) は、別の関数の動作を変更できる特殊な関数です。ここで作成するデコレータは、型アノテーション (Type Annotation) に基づいて関数の引数を検証します。型アノテーションは、関数の引数と戻り値の期待されるデータ型を指定する方法です。これは、関数が正しい入力型を受け取ることを保証し、多くのバグを防ぐことができるため、実世界のアプリケーションで一般的なユースケースです。

## 検証クラスの理解

すでに `validate.py` という名前のファイルが作成されており、いくつかの検証クラスが含まれています。検証クラスは、値が特定の条件を満たしているかどうかをチェックするために使用されます。このファイルの内容を確認するには、VSCode エディタで開く必要があります。ターミナルで以下のコマンドを実行することで開くことができます。

```bash
cd /home/labex/project
code validate.py
```

このファイルには 3 つのクラスがあります。

1. `Validator` - これは基底クラス (Base Class) です。基底クラスは、他のクラスが継承できる一般的なフレームワークまたは構造を提供します。この場合、検証の基本構造を提供します。
2. `Integer` - この検証クラスは、値が整数であることを確認するために使用されます。この検証器を使用する関数に整数でない値を渡すと、エラーが発生します。
3. `PositiveInteger` - この検証クラスは、値が正の整数であることを保証します。したがって、負の整数またはゼロを渡すと、同様にエラーが発生します。

## 検証デコレータの追加

次に、`validate.py` ファイルに `validated` という名前のデコレータ関数を追加します。このデコレータはいくつかの重要なタスクを実行します。

1. 関数の型アノテーションを調べます。型アノテーションは、関数が期待するデータの種類を示す小さな注釈のようなものです。
2. 関数に渡された引数をこれらの型アノテーションに基づいて検証します。つまり、関数に渡された値が正しい型であるかどうかをチェックします。
3. 関数の戻り値もそのアノテーションに基づいて検証します。したがって、関数が想定されたデータ型を返すことを確認します。
4. 検証に失敗した場合、有益なエラーメッセージを表示します。これらのメッセージは、どの引数の型が間違っているなど、正確に何が問題であるかを教えてくれます。

`validate.py` ファイルの末尾に以下のコードを追加します。

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

このコードは Python の `inspect` モジュールを使用しています。`inspect` モジュールを使用すると、関数などのライブオブジェクトに関する情報を取得できます。ここでは、関数のシグネチャを調べ、型アノテーションに基づいて引数を検証するために使用しています。また、`functools.wraps` も使用しています。これは、関数の名前やドキュメント文字列など、元の関数のメタデータを保持するヘルパー関数です。メタデータは、関数が何をするかを理解するのに役立つ関数に関する追加情報のようなものです。

## 検証デコレータのテスト

検証デコレータをテストするためのファイルを作成しましょう。`test_validate.py` という名前の新しいファイルを作成し、以下のコードを追加します。

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

次に、Python インタープリターでデコレータをテストします。まず、ターミナルで以下のコマンドを実行してプロジェクトディレクトリに移動し、Python インタープリターを起動します。

```bash
cd /home/labex/project
python3
```

その後、Python インタープリターで以下のコードを実行してデコレータをテストします。

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

ご覧の通り、`validated` デコレータは関数の引数と戻り値の型チェックを正常に実行しています。これは非常に有用です。型エラーがコードの奥深くまで伝播して見つけにくいバグを引き起こす代わりに、関数の境界でエラーを捕捉することができるため、コードがより堅牢になります。
