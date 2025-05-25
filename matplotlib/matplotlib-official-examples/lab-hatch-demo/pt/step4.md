# Criar um Gráfico de Barras com Múltiplas Hachuras

Você também pode usar múltiplas hachuras em seu gráfico de barras. Neste caso, usaremos um array de hachuras para criar múltiplas hachuras em nossas barras.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
