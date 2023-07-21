# MRO in Multiple Inheritance

With multiple inheritance, there is no single path to the top.
Let's take a look at an example.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

What happens when you access an attribute?

```python
e = E()
e.attr
```

An attribute search process is carried out, but what is the order? That's a problem.

Python uses _cooperative multiple inheritance_ which obeys some rules
about class ordering.

- Children are always checked before parents
- Parents (if multiple) are always checked in the order listed.

The MRO is computed by sorting all of the classes in a hierarchy
according to those rules.

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

The underlying algorithm is called the "C3 Linearization Algorithm."
The precise details aren't important as long as you remember that a
class hierarchy obeys the same ordering rules you might follow if your
house was on fire and you had to evacuate--children first, followed by
parents.
