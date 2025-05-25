# Criar o gráfico de pizza

Agora podemos criar o gráfico de pizza. Começamos definindo os objetos de figura e eixo:

```python
# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

Em seguida, definimos os parâmetros para o gráfico de pizza e o plotamos:

```python
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)
```
