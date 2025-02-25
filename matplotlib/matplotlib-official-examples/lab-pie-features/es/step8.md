# Controlar el tamaño

Podemos controlar el tamaño del gráfico circular estableciendo el parámetro `radius` de la función `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size':'smaller'}, radius=0.5)
```
