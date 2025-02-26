# 引数付きの最初のデコレータ

先ほど定義した `@logged` デコレータは、常に関数名とともに単純なメッセージを出力します。たとえば、ユーザーに何らかのカスタムメッセージを指定できるようにしたい場合があります。

引数としてフォーマット文字列を受け取り、`fmt.format(func=func)` を使って提供された関数をログメッセージにフォーマットする新しいデコレータ `@logformat(fmt)` を定義します。

```python
# sample.py
...
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y
```

これを行うには、引数を取るデコレータを定義する必要があります。テストしたときの様子は以下の通りです。

```python
>>> import sample
Adding logging to add
Adding logging to sub
Adding logging to mul
>>> sample.add(2,3)
Calling add
5
>>> sample.mul(2,3)
sample.py:mul
6
>>>
```

さらにコードを簡略化するために、元の `@logged` デコレータを `@logformat` デコレータを使ってどのように定義できるかを示します。
