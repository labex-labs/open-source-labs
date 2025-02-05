# 继承（Inheritance）的工作原理

类可以从其他类继承。

```python
class A(B, C):
   ...
```

基类（Base Class）会存储在每个类的一个元组中。

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

这提供了与父类的链接。
