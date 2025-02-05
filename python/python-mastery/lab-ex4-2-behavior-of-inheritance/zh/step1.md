# 继承的方向

Python 有两种不同的继承“方向”。第一种体现在“单继承”概念中，即一系列类从单个父类继承。例如，试试这个例子：

```python
>>> class A:
        def spam(self):
            print('A.spam')

>>> class B(A):
        def spam(self):
            print('B.spam')
            super().spam()

>>> class C(B):
        def spam(self):
            print('C.spam')
            super().spam()


>>> C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
>>> c = C()
>>> c.spam()
C.spam
B.spam
A.spam
>>>
```

注意，类 `C` 的 `__mro__` 属性按顺序编码了它的所有祖先。当你调用 `spam()` 方法时，它会按照层次结构逐个类地遍历 MRO。

在多重继承中，你会得到一种不同类型的继承，它允许将不同的类组合在一起。试试这个例子：

```python
>>> class Base:
        def spam(self):
            print('Base.spam')

>>> class X(Base):
        def spam(self):
            print('X.spam')
            super().spam()

>>> class Y(Base):
        def spam(self):
            print('Y.spam')
            super().spam()

>>> class Z(Base):
        def spam(self):
            print('Z.spam')
            super().spam()

>>>
```

注意，上面所有的类都从一个共同的父类 `Base` 继承。然而，类 `X`、`Y` 和 `Z` 彼此之间没有直接关系（没有继承链将这些类链接在一起）。

然而，看看多重继承中会发生什么：

```python
>>> class M(X,Y,Z):
        pass

>>> M.__mro__
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
>>> m = M()
>>> m.spam()
X.spam
Y.spam
Z.spam
Base.spam
>>>
```

在这里，你会看到所有的类按照子类提供的顺序堆叠在一起。假设子类重新排列类的顺序：

```python
>>> class N(Z,Y,X):
        pass

>>> N.__mro__
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
>>> n = N()
>>> n.spam()
Z.spam
Y.spam
X.spam
Base.spam
>>>
```

在这里，你会看到父类的顺序颠倒了。仔细注意在这两种情况下 `super()` 的行为。它不是委托给每个类的直接父类，而是移动到 MRO 中的下一个类。不仅如此，确切的顺序由子类控制。这相当奇怪。

还要注意，共同的父类 `Base` 用于终止 `super()` 操作的链。具体来说，`Base.spam()` 方法不会再调用任何其他方法。它也出现在 MRO 的末尾，因为它是所有组合在一起的类的父类。
