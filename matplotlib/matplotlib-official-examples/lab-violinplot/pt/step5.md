# Personalizar a aparência do gráfico

Personalizaremos a aparência do gráfico removendo os rótulos do eixo y e adicionando um título ao gráfico.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```
