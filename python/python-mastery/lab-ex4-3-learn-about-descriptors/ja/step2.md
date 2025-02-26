# 独自のディスクリプタを作成する

ノートからディスクリプタクラスを定義します。

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))
    def __delete__(self, instance):
        print('%s:__delete__' % self.name)
```

次に、このディスクリプタを使用する単純なクラスを定義してみましょう。

```python
>>> class Foo:
        a = Descriptor('a')
        b = Descriptor('b')
        c = Descriptor('c')

>>> f = Foo()
>>> f
<__main__.Foo object at 0x38e130> <class __main__.Foo>
>>> f.a
a:__get__
>>> f.b
b:__get__
>>> f.a = 23
a:__set__ 23
>>> del f.a
a:__delete__
>>>
```

特定の属性に対してドット演算子をキャプチャしたことを考えてみましょう。
