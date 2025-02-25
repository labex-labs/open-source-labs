# Agregar etiquetas a los segmentos

Podemos agregar etiquetas a los segmentos pasando una lista de etiquetas al parámetro `labels` de la función `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```
