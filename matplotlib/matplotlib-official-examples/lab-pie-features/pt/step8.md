# Controlando o Tamanho

Podemos controlar o tamanho do gráfico de pizza definindo o parâmetro `radius` da função `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, radius=0.5)
```
