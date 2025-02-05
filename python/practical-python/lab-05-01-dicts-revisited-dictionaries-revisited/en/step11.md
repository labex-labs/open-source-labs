# Reading Attributes with Single Inheritance

In inheritance hierarchies, attributes are found by walking up the inheritance tree in order.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

With single inheritance, there is single path to the top. You stop with the first match.
