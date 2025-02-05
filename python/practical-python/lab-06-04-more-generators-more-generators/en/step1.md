# Generator Expressions

A generator version of a list comprehension.

```python
>>> a = [1,2,3,4]
>>> b = (2*x for x in a)
>>> b
<generator object at 0x58760>
>>> for i in b:
...   print(i, end=' ')
...
2 4 6 8
>>>
```

Differences with List Comprehensions.

- Does not construct a list.
- Only useful purpose is iteration.
- Once consumed, can't be reused.

General syntax.

```python
(<expression> for i in s if <conditional>)
```

It can also serve as a function argument.

```python
sum(x*x for x in a)
```

It can be applied to any iterable.

```python
>>> a = [1,2,3,4]
>>> b = (x*x for x in a)
>>> c = (-x for x in b)
>>> for i in c:
...   print(i, end=' ')
...
-1 -4 -9 -16
>>>
```

The main use of generator expressions is in code that performs some calculation on a sequence, but only uses the result once. For example, strip all comments from a file.

```python
f = open('somefile.txt')
lines = (line for line in f if not line.startswith('#'))
for line in lines:
    ...
f.close()
```

With generators, the code runs faster and uses little memory. It's like a filter applied to a stream.
