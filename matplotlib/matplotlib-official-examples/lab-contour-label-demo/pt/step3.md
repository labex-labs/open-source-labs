# Rotulando contornos com strings arbitrárias usando um dicionário

Também podemos rotular contornos com strings arbitrárias usando um dicionário. Isso nos permitirá rotular os contornos com rótulos personalizados. Neste exemplo, usaremos uma lista de strings para rotular os contornos.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
