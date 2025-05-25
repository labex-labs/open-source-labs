# Ordenação de Listas

Listas podem ser ordenadas "in-place" (no local).

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Reverse order
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# It works with any ordered data
s = ['foo', 'bar', 'spam']
s.sort()                    # ['bar', 'foo', 'spam']
```

Use `sorted()` se você quiser criar uma nova lista em vez disso:

```python
t = sorted(s)               # s unchanged, t holds sorted values
```
