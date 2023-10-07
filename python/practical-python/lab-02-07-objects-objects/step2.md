# Assignment example

Consider this code fragment.

```python
a = [1,2,3]
b = a
c = [a,b]
```

A picture of the underlying memory operations. In this example, there is only one list object `[1,2,3]`, but there are four different references to it.

![References](./assets/references.png)

This means that modifying a value affects _all_ references.

```python
>>> a.append(999)
>>> a
[1,2,3,999]
>>> b
[1,2,3,999]
>>> c
[[1,2,3,999], [1,2,3,999]]
>>>
```

Notice how a change in the original list shows up everywhere else (yikes!). This is because no copies were ever made. Everything is pointing to the same thing.
