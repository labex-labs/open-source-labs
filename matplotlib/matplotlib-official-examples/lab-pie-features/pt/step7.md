# Explodindo as Fatias

Podemos explodir uma ou mais fatias do gráfico de pizza passando uma lista de valores para o parâmetro `explode` da função `pie()`.

```python
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
