# デコレータで関数のメタデータを保持する

Python では、デコレータは関数の動作を変更できる強力なツールです。ただし、デコレータを使って関数をラップすると、少し問題があります。デフォルトでは、元の関数のメタデータ（名前、ドキュメント文字列（docstring）、アノテーションなど）が失われます。メタデータは、イントロスペクション（コードの構造を調べること）やドキュメント生成に役立つため重要です。まずはこの問題を確認してみましょう。

WebIDE でターミナルを開きます。デコレータを使ったときに何が起こるかを確認するために、いくつかの Python コマンドを実行します。以下のコマンドで、デコレータでラップされた単純な関数 `add` を作成し、その関数とドキュメント文字列を出力します。

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

これらのコマンドを実行すると、次のような出力が表示されます。

```
<function wrapper at 0x...>
None
```

関数名が `add` ではなく `wrapper` と表示されていることに注意してください。また、ドキュメント文字列は `'Adds two things'` であるはずが、`None` となっています。これは、イントロスペクションツールやドキュメント生成ツールなど、このメタデータに依存するツールを使用する際に大きな問題となります。

## functools.wraps で問題を解決する

Python の `functools` モジュールが助けになります。このモジュールには、関数のメタデータを保持するのに役立つ `wraps` デコレータが用意されています。`logged` デコレータを `wraps` を使うように修正する方法を見てみましょう。

1. まず、WebIDE で `logcall.py` ファイルを開きます。ターミナルで次のコマンドを実行すると、プロジェクトディレクトリに移動できます。

```bash
cd ~/project
```

2. 次に、`logcall.py` の `logged` デコレータを次のコードで更新します。ここで重要なのは `@wraps(func)` デコレータです。これにより、元の関数 `func` のすべてのメタデータがラッパー関数にコピーされます。

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. `@wraps(func)` デコレータは重要な役割を果たします。元の関数 `func` のすべてのメタデータ（名前、ドキュメント文字列、アノテーションなど）を取得し、`wrapper` 関数に付加します。これにより、デコレートされた関数を使用するときに、正しいメタデータが保持されます。

4. 改良したデコレータをテストしてみましょう。ターミナルで次のコマンドを実行します。

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

すると、次のように表示されるはずです。

```
<function add at 0x...>
Adds two things
```

素晴らしい！関数名とドキュメント文字列が保持されています。これは、デコレータが期待通りに動作し、元の関数のメタデータが無傷であることを意味します。

## validate.py のデコレータを修正する

次に、`validate.py` の `validated` デコレータにも同じ修正を適用しましょう。このデコレータは、関数のアノテーションに基づいて関数の引数と戻り値の型を検証するために使用されます。

1. WebIDE で `validate.py` を開きます。

2. `validated` デコレータを `@wraps` デコレータで更新します。次のコードはその方法を示しています。`validated` デコレータ内の `wrapper` 関数に `@wraps(func)` デコレータを追加することで、メタデータが保持されます。

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
```

3. `validated` デコレータがメタデータを保持するようになったことをテストしましょう。ターミナルで次のコマンドを実行します。

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

次のように表示されるはずです。

```
<function multiply at 0......>
Multiplies two integers
```

これで、`logged` と `validated` の両方のデコレータが、デコレートする関数のメタデータを適切に保持するようになりました。これにより、これらのデコレータを使用するときに、関数は依然として元の名前、ドキュメント文字列、アノテーションを持ち、コードの可読性と保守性に非常に役立ちます。
