# Personalizando e Salvando o Gráfico

Podemos personalizar ainda mais o gráfico usando as opções de personalização do Matplotlib. Também podemos salvar o gráfico em um arquivo.

```python
# Personalizando e salvando o gráfico
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("Concentração de NO$_2$")
fig.savefig("no2_concentrations.png")
plt.show()
```
