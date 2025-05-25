# Modificando a Sombra

Podemos modificar a sombra do gráfico de pizza passando um dicionário de argumentos para o parâmetro `shadow` da função `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
```
