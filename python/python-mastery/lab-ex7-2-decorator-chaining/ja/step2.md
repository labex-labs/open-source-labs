# 引数を持つデコレータの作成

これまで、常に固定メッセージを出力する `@logged` デコレータを使用してきました。では、メッセージの形式をカスタマイズしたい場合はどうすればよいでしょうか？このセクションでは、引数を受け取る新しいデコレータを作成する方法を学び、デコレータの使用方法により柔軟性を持たせます。

## パラメータ付きデコレータの理解

パラメータ付きデコレータは特殊な関数の一種です。他の関数を直接変更するのではなく、デコレータを返します。パラメータ付きデコレータの一般的な構造は次のようになります。

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

コードで `@decorator_with_args(value1, value2)` を使用すると、Python はまず `decorator_with_args(value1, value2)` を呼び出します。この呼び出しは実際のデコレータを返し、それが `@` 構文の後に続く関数に適用されます。この二段階のプロセスが、パラメータ付きデコレータの動作の鍵となります。

## logformat デコレータの作成

フォーマット文字列（format string）を引数として受け取る `@logformat(fmt)` デコレータを作成しましょう。これにより、ログメッセージをカスタマイズできます。

1. WebIDE で `logcall.py` を開き、新しいデコレータを追加します。以下のコードは、既存の `logged` デコレータと新しい `logformat` デコレータの定義方法を示しています。

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

`logformat` デコレータでは、外側の関数 `logformat` がフォーマット文字列 `fmt` を引数として受け取ります。そして、ターゲット関数を変更する実際のデコレータである `decorator` 関数を返します。

2. 次に、`sample.py` を修正して新しいデコレータをテストしましょう。以下のコードは、異なる関数に `logged` と `logformat` の両方のデコレータを使用する方法を示しています。

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

ここでは、`add` 関数と `sub` 関数は `logged` デコレータを使用し、`mul` 関数はカスタムフォーマット文字列で `logformat` デコレータを使用しています。

3. 更新した `sample.py` を実行して結果を確認します。ターミナルを開き、次のコマンドを実行します。

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

次のような出力が表示されるはずです。

```
Calling add
5
sample.py:mul
6
```

この出力から、`logged` デコレータが期待通りに関数名を出力し、`logformat` デコレータがカスタムフォーマット文字列を使用してファイル名と関数名を出力していることがわかります。

## logformat を使用して logged デコレータを再定義する

より柔軟な `logformat` デコレータができたので、これを使用して元の `logged` デコレータを再定義しましょう。これにより、コードの再利用が可能になり、一貫したログフォーマットを維持できます。

1. `logcall.py` を次のコードで更新します。

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

ここでは、ラムダ関数を使用して、`logformat` デコレータを基に `logged` デコレータを定義しています。ラムダ関数は関数 `func` を受け取り、特定のフォーマット文字列で `logformat` デコレータを適用します。

2. 再定義した `logged` デコレータが引き続き機能することをテストします。ターミナルを開き、次のコマンドを実行します。

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

次のように表示されるはずです。

```
Calling greet
Hello, World
```

これは、再定義した `logged` デコレータが期待通りに動作し、`logformat` デコレータを成功裏に再利用して一貫したログフォーマットを実現したことを示しています。
