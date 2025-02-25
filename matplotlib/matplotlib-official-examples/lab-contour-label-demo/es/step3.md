# Etiqueta los contornos con cadenas arbitrarias usando un diccionario

También podemos etiquetar los contornos con cadenas arbitrarias usando un diccionario. Esto nos permitirá etiquetar los contornos con etiquetas personalizadas. En este ejemplo, usaremos una lista de cadenas para etiquetar los contornos.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first','second', 'third', 'fourth', 'fifth','sixth','seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
