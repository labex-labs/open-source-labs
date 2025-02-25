# Personalizar los patrones de relleno

Podemos personalizar los patrones de relleno de los segmentos pasando una lista de patrones de relleno al parámetro `hatch` de la función `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```
