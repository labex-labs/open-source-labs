# 多重继承（Multiple Inheritance）中的 MRO

在多重继承中，没有单一的路径通向顶层。让我们来看一个例子。

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

当你访问一个属性时会发生什么呢？

```python
e = E()
e.attr
```

会进行属性搜索过程，但搜索顺序是怎样的呢？这就是个问题了。

Python 使用“协作式多重继承（cooperative multiple inheritance）”，它遵循一些关于类排序的规则。

- 总是先检查子类，再检查父类
- （如果有多个）父类总是按照列出的顺序进行检查

MRO 是根据这些规则对层次结构中的所有类进行排序计算得出的。

```python
>>> E.__mro__
(
  <class 'E'>,
  <class 'C'>,
  <class 'A'>,
  <class 'D'>,
  <class 'B'>,
  <class 'object'>)
>>>
```

底层的算法被称为“C3 线性化算法（C3 Linearization Algorithm）”。只要你记住，类层次结构遵循的排序规则就像你的房子着火了，你必须疏散时遵循的规则一样——先救孩子，再救父母，具体细节并不重要。
