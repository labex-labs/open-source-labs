# シンプルなジェネレータ

反復処理をカスタマイズしたいときは、常にジェネレータ関数を考えるべきです。書きやすいです。必要な反復処理のロジックを実行し、値を発行するために `yield` を使用する関数を作成するだけです。

たとえば、このジェネレータを試してみてください。これは、分数ステップで数値の範囲を反復処理できるようにします（組み込み関数 `range()` ではサポートされていません）。

```python
>>> def frange(start,stop,step):
        while start < stop:
            yield start
            start += step

>>> for x in frange(0, 2, 0.25):
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```

ジェネレータを反復処理することは、一度だけの操作です。たとえば、2回反復処理しようとするとどうなるか見てみましょう。

```python
>>> f = frange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

>>>
```

同じシーケンスを反復処理したい場合は、再度 `frange()` を呼び出してジェネレータを再作成する必要があります。あるいは、すべてをクラスにまとめることもできます。

```python
>>> class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
        def __iter__(self):
            n = self.start
            while n < self.stop:
                yield n
                n += self.step

>>> f = FRange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```
