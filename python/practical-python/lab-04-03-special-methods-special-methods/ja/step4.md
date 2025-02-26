# 要素アクセス用の特殊メソッド

これらは、コンテナを実装するためのメソッドです。

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

これらをクラスで使用することができます。

```python
class Sequence:
    def __len__(self):
     ...
    def __getitem__(self,a):
     ...
    def __setitem__(self,a,v):
     ...
    def __delitem__(self,a):
     ...
```
