# Étiqueter les contours avec des chaînes arbitraires à l'aide d'un dictionnaire

Nous pouvons également étiqueter les contours avec des chaînes arbitraires à l'aide d'un dictionnaire. Cela nous permettra d'étiqueter les contours avec des étiquettes personnalisées. Dans cet exemple, nous utiliserons une liste de chaînes pour étiqueter les contours.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first','second', 'third', 'fourth', 'fifth','sixth','seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
