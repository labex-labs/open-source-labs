# Ejes polares

Podemos crear una cuadrícula de `Axes` polares pasando el parámetro `projection='polar'` a la función `subplots()`.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
