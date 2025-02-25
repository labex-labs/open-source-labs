# Separar los segmentos

Podemos separar uno o más segmentos del gráfico circular pasando una lista de valores al parámetro `explode` de la función `pie()`.

```python
explode = (0, 0.1, 0, 0)  # solo "separa" el segundo segmento (es decir, 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
