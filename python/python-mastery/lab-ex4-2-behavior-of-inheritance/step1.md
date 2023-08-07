# The directions of inheritance

Python has two different "directions" of inheritance. The first is found in the concept of "single inheritance" where a series of classes inherit from a single parent. For example, try this example:

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

Observe that the `__mro__` attribute of class `C` encodes all of its ancestors in order. When you invoke the `spam()` method, it walks the MRO class-by-class up the hierarchy.

With multiple inheritance, you get a different kind of inheritance that allows different classes to be composed together. Try this example:

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

Notice that all of the classes above inherit from a common parent `Base`. However, the classes `X`, `Y`, and `Z` are not directly related to each other (there is no inheritance chain linking those classes together).

However, watch what happens in multiple inheritance:

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

Here, you see all of the classes stack together in the order supplied by the subclass. Suppose the subclass rearranges the class order:

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

Here, you see the order of the parents flip around. Carefully pay attention to what `super()` is doing in both cases. It doesn't delegate to the immediate parent of each class--instead, it moves to the next class on the MRO. Not only that, the exact order is controlled by the child. This is pretty weird.

Also notice that the common parent `Base` serves to terminate the chain of `super()` operations. Specifically, the `Base.spam()` method does not call any further methods. It also appears at the end of the MRO since it is the parent to all of the classes being composed together.
