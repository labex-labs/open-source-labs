# Adicionar Lenda e Exibir o Gráfico

Adicionamos uma legenda ao gráfico para diferenciar os modelos sem pesos e com pesos. Em seguida, exibimos o gráfico.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["sem pesos", "com pesos"],
    loc="lower left",
)

ax.set(xticks=(), yticks=())
plt.show()
```
