# Personalizar o Gráfico de Setas

O terceiro passo é personalizar o gráfico de setas. Podemos alterar a propriedade da seta a ser exibida usando o parâmetro `display`. Também podemos alterar a forma da seta usando o parâmetro `shape`. Podemos ajustar a largura e a separação das setas usando os parâmetros `max_arrow_width` e `arrow_sep`, respectivamente. Podemos alterar a transparência das setas usando o parâmetro `alpha`. Também podemos alterar a cor do rótulo usando o parâmetro `labelcolor`.

```python
# Plot the arrow graph with customizations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
