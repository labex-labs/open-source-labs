# Modificar la sombra

Podemos modificar la sombra del gráfico circular pasando un diccionario de argumentos al parámetro `shadow` de la función `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none','shade': 0.9}, startangle=90)
```
