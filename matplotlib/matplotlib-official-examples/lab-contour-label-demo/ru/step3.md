# Метка контуров произвольными строками с использованием словаря

Мы также можем метить контуру произвольными строками с использованием словаря. Это позволит нам метить контуры пользовательскими метками. В этом примере мы будем использовать список строк для метки контуров.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first', 'second', 'third', 'fourth', 'fifth','sixth','seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
