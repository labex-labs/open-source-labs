# Rotulagem de Barras Usando String de Formatação no Estilo `{}`

Nesta etapa, mostraremos como usar uma string de formatação no estilo `{}` para formatar rótulos de barras. Usaremos alguns dados sobre vendas de gelato por sabor.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
