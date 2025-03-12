# 引数を持つ型強制デコレータの作成

前のステップでは、`@validated` デコレータについて学びました。このデコレータは、Python 関数で型アノテーションを強制するために使用されます。型アノテーションは、関数の引数と戻り値の期待される型を指定する方法です。今回は、さらに一歩進んで、型指定を引数として受け取ることができる、より柔軟なデコレータを作成します。これにより、各引数と戻り値に対して、より明示的に型を定義することができます。

## 目標の理解

私たちの目標は、`@enforce()` デコレータを作成することです。このデコレータを使用すると、キーワード引数を使って型制約を指定することができます。以下は、その動作の例です。

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

この例では、`@enforce` デコレータを使用して、`add` 関数の `x` と `y` 引数が `Integer` 型であるべきこと、および戻り値も `Integer` 型であるべきことを指定しています。このデコレータは、前の `@validated` デコレータと同様の動作をしますが、型指定に対するコントロールがより強化されています。

## enforce デコレータの作成

1. まず、WebIDE で `validate.py` ファイルを開きます。このファイルに新しいデコレータを追加します。追加するコードは次のとおりです。

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

このコードが何をするかを分解してみましょう。`Integer` クラスは、カスタム型を定義するために使用されます。`validated` デコレータは、関数の型アノテーションに基づいて、関数の引数と戻り値の型をチェックします。`enforce` デコレータは、私たちが作成する新しいデコレータです。これは、各引数と戻り値の型を指定するキーワード引数を受け取ります。`enforce` デコレータの `wrapper` 関数内では、引数と戻り値の型が指定された型と一致するかどうかをチェックします。一致しない場合は、`TypeError` を発生させます。

2. 次に、新しい `@enforce` デコレータをテストしましょう。いくつかのテストケースを実行して、期待通りに動作するかどうかを確認します。テストを実行するコードは次のとおりです。

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

このテストコードでは、まず `@enforce` デコレータを使用して `add` 関数を定義します。次に、有効な引数で `add` 関数を呼び出します。これはエラーなく動作するはずです。次に、無効な引数で `add` 関数を呼び出します。これは `TypeError` を発生させるはずです。最後に、誤った型の値を返す `bad_add` 関数を定義します。これも `TypeError` を発生させるはずです。

このテストコードを実行すると、次のような出力が表示されるはずです。

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

この出力は、`@enforce` デコレータが正しく動作していることを示しています。引数または戻り値の型が指定された型と一致しない場合、`TypeError` を発生させます。

## 2 つのアプローチの比較

`@validated` デコレータと `@enforce` デコレータはどちらも、型制約を強制するという同じ目標を達成しますが、方法が異なります。

1. `@validated` デコレータは、Python の組み込み型アノテーションを使用します。以下は例です。

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   このアプローチでは、型アノテーションを使用して、関数定義内で直接型を指定します。これは Python の組み込み機能であり、統合開発環境（IDE）でより良いサポートが提供されます。IDE はこれらの型アノテーションを使用して、コード補完、型チェック、その他の便利な機能を提供することができます。

2. 一方、`@enforce` デコレータは、キーワード引数を使用して型を指定します。以下は例です。

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   このアプローチは、型指定を直接デコレータの引数として渡しているため、より明示的です。他のアノテーションシステムに依存するライブラリを使用する場合に便利です。

各アプローチにはそれぞれ利点があります。型アノテーションは Python のネイティブな機能であり、IDE のサポートが良好です。一方、`@enforce` アプローチは、より柔軟性と明示性を提供します。作業しているプロジェクトに応じて、最適なアプローチを選択することができます。
