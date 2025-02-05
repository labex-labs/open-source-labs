# 通过单继承（Single Inheritance）读取属性（Attribute）

在继承（Inheritance）层次结构中，属性是通过按顺序遍历继承树来查找的。

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

对于单继承，存在一条通向顶层的单一路径。找到第一个匹配项时，查找就会停止。
