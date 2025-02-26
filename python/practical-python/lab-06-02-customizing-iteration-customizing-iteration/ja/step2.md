# ジェネレータ

ジェネレータは、反復処理を定義する関数です。

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

たとえば：

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

ジェネレータは、`yield` 文を使用する任意の関数です。

ジェネレータの動作は通常の関数とは異なります。ジェネレータ関数を呼び出すと、ジェネレータオブジェクトが作成されます。関数はすぐに実行されません。

```python
def countdown(n):
    # 出力文を追加
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
```

```python
>>> x = countdown(10)
# 出力文は表示されない
>>> x
# xはジェネレータオブジェクト
<generator object at 0x58490>
>>>
```

関数は `__next__()` 呼び出し時にのみ実行されます。

```python
>>> x = countdown(10)
>>> x
<generator object at 0x58490>
>>> x.__next__()
Counting down from 10
10
>>>
```

`yield` は値を生成しますが、関数の実行を中断します。関数は次の `__next__()` 呼び出し時に再開されます。

```python
>>> x.__next__()
9
>>> x.__next__()
8
```

ジェネレータが最終的に返すと、反復処理はエラーを発生させます。

```python
>>> x.__next__()
1
>>> x.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```

_注：ジェネレータ関数は、for文がリスト、タプル、辞書、ファイルなどで使用するのと同じ低レベルのプロトコルを実装しています。_
