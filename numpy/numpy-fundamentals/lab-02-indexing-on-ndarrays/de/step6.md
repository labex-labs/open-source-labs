# Indexierung mit flachem Iterator

Das Attribut `x.flat` gibt einen Iterator zurück, der verwendet werden kann, um das gesamte Array in C-stetiger Weise zu iterieren. Mit diesem Iterator kann auch mit dem grundlegenden Slicing oder dem fortgeschrittenen Indexieren indiziert werden.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Ausgabe: [1, 2, 3, 4]
```
