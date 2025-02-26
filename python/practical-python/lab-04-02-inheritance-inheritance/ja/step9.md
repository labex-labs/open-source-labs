# 「is a」関係

継承は型関係を確立します。

```python
class Shape:
...

class Circle(Shape):
...
```

オブジェクトインスタンスを確認します。

```python
>>> c = Circle(4.0)
>>> isinstance(c, Shape)
True
>>>
```

_重要: 理想的には、親クラスのインスタンスで機能する任意のコードは、子クラスのインスタンスでも機能するはずです。_
