# 契約型プログラミング

契約による設計とも呼ばれ、アサーションを十分に利用することはソフトウェアを設計するためのアプローチです。ソフトウェアのコンポーネントに対して正確なインターフェイス仕様を定義するようソフトウェア設計者に求めます。

たとえば、関数のすべての入力にアサーションを置くことができます。

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

入力をチェックすることで、適切な引数を使用していない呼び出し元を直ちにキャッチすることができます。

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
