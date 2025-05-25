# Definir os Parâmetros do Gráfico de Barras

O próximo passo é definir os parâmetros para o gráfico de barras. Definiremos as localizações x para os grupos, a largura das barras e os rótulos para os x-ticks.

```python
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
