# Plotar as curvas de aprendizagem para cada conjunto de dados

Finalmente, podemos plotar as curvas de aprendizagem para cada conjunto de dados usando a função `plot_on_dataset`. Criaremos um gráfico 2x2 e plotaremos cada conjunto de dados em um eixo separado.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
