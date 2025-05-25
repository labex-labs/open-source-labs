# Eixos Polares

Podemos criar uma grade de `Axes` polares passando o parâmetro `projection='polar'` para a função `subplots()`.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
