# Personalizar el aspecto del gráfico

Personalizaremos el aspecto del gráfico eliminando las etiquetas del eje y y agregando un título al gráfico.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```
