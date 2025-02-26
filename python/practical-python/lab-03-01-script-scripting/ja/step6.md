# 関数の定義

関数は、どんな順序でも「定義」できます。

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# または
def bar(x):
    statements

def foo(x):
    bar(x)
```

関数は、プログラム実行中に実際に「使用」（または呼び出し）される前にのみ定義する必要があります。

```python
foo(3)        # foo は既に定義されている必要があります
```

スタイリッシュには、関数が「下から上」の形式で定義されるのが一般的です。
