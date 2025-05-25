# Adicionar Anotação de Seta

Setas podem ser usadas para apontar características ou tendências específicas em um gráfico. Nesta etapa, adicionaremos uma seta ao gráfico que aponta para o valor máximo.

```python
# Find the maximum value
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# Add arrow annotation
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```
