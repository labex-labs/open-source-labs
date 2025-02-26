# 演習7.10：実行時間を計測するデコレータ

関数を定義すると、その名前とモジュールが `__name__` と `__module__` 属性に格納されます。たとえば：

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

`timethis.py` というファイルに、関数の実行にどれくらいの時間がかかるかを表示する追加のロジックで関数をラップするデコレータ関数 `timethis(func)` を書きます。これを行うには、次のような計測呼び出しで関数を囲みます：

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

ここに、あなたのデコレータがどのように機能するかの例を示します：

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

考察：この `@timethis` デコレータは、どんな関数定義の前にも配置できます。したがって、パフォーマンスチューニングの診断ツールとして使用できます。
