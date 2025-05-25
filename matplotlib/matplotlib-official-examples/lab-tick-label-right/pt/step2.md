# Definir os rótulos de marcação do eixo y padrão à direita

Podemos definir os rótulos de marcação do eixo y padrão no lado direito do gráfico usando o seguinte código:

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
